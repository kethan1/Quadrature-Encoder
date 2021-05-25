#include <iostream>
#include <pigpio.h>
#include <unistd.h>
#include "Encoder.hpp"


/*

REQUIRES

A rotary encoder contacts A and B connected to separate gpios and
the common contact connected to Pi ground.

TO BUILD

g++ -o rot_enc_cpp.out test_rotary_encoder.cpp rotary_encoder.cpp -lpigpio -lrt

TO RUN

sudo ./rot_enc_cpp.out

*/

int main() {
    if (gpioInitialise() < 0) return 1;

    Encoder encoder1(23, 24);

    usleep(4000000);

    encoder1.cancel_callbacks();

    gpioTerminate();
}
