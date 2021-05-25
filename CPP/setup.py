#!/usr/bin/env python3

from distutils.core import setup, Extension

encoder_module = Extension("_encoder",
    sources = ["encoder_wrap.cxx", "Encoder.cpp"],
    libraries = ["pigpio"]
)

setup(name = "Encoder",
      author = "Kethan Vegunta",
      description = "An encoder module written in C++.",
      ext_modules = [encoder_module],
      py_modules = ["encoder"]
)