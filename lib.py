import ctypes
import numpy as np


lib = ctypes.CDLL('./lib.so')

# dft function
lib.dft.restype = None	
lib.dft.argtypes = [np.ctypeslib.ndpointer( flags="C"), ctypes.c_int, np.ctypeslib.ndpointer(flags="C")]

# dft imag
lib.dft_imag.restype = None	
lib.dft_imag.argtypes = [np.ctypeslib.ndpointer( flags="C"),  ctypes.c_int, np.ctypeslib.ndpointer(flags="C")]

# dft real 
lib.dft_real.restype = None	
lib.dft_real.argtypes = [np.ctypeslib.ndpointer( flags="C"), ctypes.c_int, np.ctypeslib.ndpointer(flags="C")]


# fft function
lib.fft.restype = None	
lib.fft.argtypes = [np.ctypeslib.ndpointer( flags="C"), ctypes.c_int]

# fft real function
lib.fft_real.restype = None	
lib.fft_real.argtypes = [np.ctypeslib.ndpointer( flags="C"), ctypes.c_int, np.ctypeslib.ndpointer(flags="C")]

# fft imag function
lib.fft_imag.restype = None	
lib.fft_imag.argtypes = [np.ctypeslib.ndpointer( flags="C"), ctypes.c_int, np.ctypeslib.ndpointer(flags="C")]



class c_complex(ctypes.Structure):
    # Complex number, compatible with std::complex layout
    _fields_ = [("real", ctypes.c_double), ("imag", ctypes.c_double)]

    def __init__(self, pycomplex):
        # Init from Python complex
        self.real = pycomplex.real
        self.imag = pycomplex.imag


def complex_check(l):
        arr_t = c_complex * len(l)
        a = arr_t(*(c_complex(r) for r in l))
        b = np.copy(a)
        return b



def dft(signal):
    signal = complex_check(signal)
    output = np.copy(signal)
    lib.dft(signal, len(signal), output)
    return output

def rdft(signal):
    signal = complex_check(signal)
    output = np.empty((len(signal)),dtype=np.float64)
    lib.dft_real(signal, len(signal), output)
    return output

def idft(signal):
    signal = complex_check(signal)
    output = np.empty((len(signal)),dtype=np.float64)
    lib.dft_imag(signal, len(signal), output)
    return output

def fft(signal):
    signal = complex_check(signal)
    output = np.copy(signal)
    lib.fft(output, len(output))
    return output

def rfft(signal):
    signal = complex_check(signal)
    output = np.empty((len(signal)),dtype=np.float64)
    lib.fft_real(signal, len(signal),output)
    return output

def ifft(signal):
    signal = complex_check(signal)
    output = np.empty((len(signal)),dtype=np.float64)
    lib.fft_imag(signal, len(signal), output)
    return output




# test2 = [1.5, 70.0, 81.0, 90.5, 0.0, 2.0, 15.7, 0.0]


# f = np.fft.fft(test2)
# print("np fft")
# print(f)

# print("dft")
# df = dft(test2)
# print(df)

# print("real")
# rdf = rdft(test2)
# print(rdf)


# print("imag")
# idf = idft(test2)
# print(idf)



# print("fft")
# df = fft(test2)
# print(df)

# print("real")
# rdf = rfft(test2)
# print(rdf)


# print("imag")
# idf = ifft(test2)
# print(idf)