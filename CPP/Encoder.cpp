#include "Encoder.hpp"
#include <iostream>
#include <pigpio.h>

void initialise() {
    gpioInitialise();
}

void Encoder::_pulse(int gpio, int level, uint32_t tick, void *user) {
    /*
        Need a static callback to link with C.
    */

    Encoder *self = (Encoder *) user;

    if (gpio == self->gpioA) self->levA = level; else self->levB = level;

    if (gpio != self->lastGpio) { /* debounce */
        self->lastGpio = gpio;

        if ((gpio == self->gpioA) && (level == 1)) {
            if (self->levB) self->steps++;
            // std::cout << self->steps << std::endl;
        }
        else if ((gpio == self->gpioB) && (level == 1)) {
            if (self->levA) { 
                self->steps--;
                std::cout << "BadBad" << std::endl;
            }
        }
    }
}

Encoder::Encoder(int aGpioA, int aGpioB) {
    gpioA = aGpioA;
    gpioB = aGpioB;

    levA = 0;
    levB = 0;

    steps = 0;

    lastGpio = -1;

    gpioSetMode(aGpioA, PI_INPUT);
    gpioSetMode(aGpioB, PI_INPUT);

    /* pull up is needed as encoder common is grounded */

    gpioSetPullUpDown(aGpioA, PI_PUD_UP);
    gpioSetPullUpDown(aGpioB, PI_PUD_UP);

    /* monitor encoder level changes */

    gpioSetAlertFuncEx(aGpioA, _pulse, this);
    gpioSetAlertFuncEx(aGpioB, _pulse, this);
}

void Encoder::cancel_callbacks(void) {
    gpioSetAlertFuncEx(gpioA, NULL, this);
    gpioSetAlertFuncEx(gpioB, NULL, this);
}

Encoder::~Encoder() {
    cancel_callbacks();
    gpioTerminate();
}

int Encoder::getSteps() {
    return steps;
}

void Encoder::resetSteps() {
    steps = 0;
}
