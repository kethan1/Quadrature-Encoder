#!/bin/bash

g++ -o CPP_Encoder.out test_Encoder.cpp Encoder.cpp -lpigpio -lrt
sudo ./CPP_Encoder.out