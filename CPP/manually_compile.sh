#!/bin/bash

# Manually compile
swig -c++ -python -py3 encoder.i
g++ -c -fPIC Encoder.cpp encoder_wrap.cxx -I/usr/include/python3.7
g++ -shared Encoder.o encoder_wrap.o -o _encoder.so -lpigpio
