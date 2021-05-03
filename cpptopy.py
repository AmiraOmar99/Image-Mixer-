import ctypes
import numpy


lib = ctypes.CDLL('./lib.so')

lib.dft_real.restype = numpy.ctypeslib.ndpointer(dtype=numpy.float64)	
lib.dft_real.argtypes = [numpy.ctypeslib.ndpointer(dtype=numpy.int32), ctypes.c_int]
signal = numpy.arange(1, 11, 1, numpy.int32)

# lib.dft_real.restype = ctypes.pointer(ctypes.c_double)
# lib.dft_real.argtypes = [ctypes.c_int, ctypes.pointer(ctypes.c_double)]
# signal = [1,1,1,1,1,1,1,1,1,1]
# x = lib.dft_real(ctypes.byref(signal), len(signal))

x = lib.dft_real(signal, len(signal))

print(x[1])