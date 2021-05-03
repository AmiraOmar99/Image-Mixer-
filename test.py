import ctypes
import numpy as np


lib = ctypes.CDLL('./lib.so')

lib.dft.restype = None	
lib.dft.argtypes = [np.ctypeslib.ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"), ctypes.c_int, np.ctypeslib.ndpointer(ctypes.c_double, flags="C_CONTIGUOUS")]
# lib.dft.argtypes = [np.ctypeslib.ndpointer(np.complex64, flags="C_CONTIGUOUS"), ctypes.c_int, np.ctypeslib.ndpointer(np.complex64, flags="C_CONTIGUOUS")]


lib.fft2.restype = None	
lib.fft2.argtypes = [np.ctypeslib.ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"), ctypes.c_int]
# l = [1,1,1,1,1,1,1,1,1,1]
# signal = np.arange(1.0, 11, 1, np.float64)
# signal = np.array(l,np.float64)
# testdft = np.array([])
# testdft = np.copy(signal)
# lib.dft(signal, len(signal), testdft)

N = 1024
Ts = 1/N
t = np.arange(0,10+Ts,Ts)
x = 1* np.cos(2*np.pi*500*t)
y = 0* np.sin(2*np.pi*3*t)
# print(t)
# print('1')
signal = np.column_stack((x,y))
# print(len(signal))
# print('1')
# ff = np.fft.fft(signal)

# print(ff[500]/N)

# lib.fft2(signal, len(signal))

# print(signal[500]/N)
# output = np.copy(signal)
output = np.column_stack((x,y))

# print('2')


# lib.dft(signal, len(signal), output)

lib.dft(signal, 1024 , output)

print('np fft')

ff = np.fft.fft(signal)

print(ff[500])

print('dft')
print(output[500]/N)




# signal =[1.5, 70.0, 81.0, 90.5, 0.0, 2.0, 15.7, 0.0]

# test = np.array(signal, np.complex64)
# test = np.array(signal, np.float64)

# out  = np.fft.fft(test)

# print(out[1])

# output = np.empty((len(signal)), dtype = np.complex64)

# lib.dft(test, len(test), output)

# print(output[1])

# lib.fft2(test, len(test))
# print(test[1])