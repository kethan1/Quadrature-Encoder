_encoder.so: encoder_wrap.cxx Encoder.cpp
	python3 setup.py build_ext --inplace
encoder.py encoder_wrap.cxx: encoder.i Encoder.hpp
	swig -c++ -python -py3 encoder.i
clean:
	rm -rf __pycache__ build _encoder*.so encoder.py encoder_wrap.cxx
test: _encoder.so
	sudo python3 tester.py
