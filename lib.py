import ctypes
import numpy as np


lib = ctypes.CDLL('./lib.so')

# dft function
lib.dft.restype = None	
lib.dft.argtypes = [np.ctypeslib.ndpointer( flags="C"), ctypes.c_int, np.ctypeslib.ndpointer(flags="C")]


# dft parts function (real, imag)
lib.dft_part.restype = None	
lib.dft_part.argtypes = [np.ctypeslib.ndpointer( flags="C"), ctypes.c_int, np.ctypeslib.ndpointer(flags="C"), ctypes.c_bool, ctypes.c_bool]


# fft function
lib.fft.restype = None	
lib.fft.argtypes = [np.ctypeslib.ndpointer( flags="C"), ctypes.c_int]

# fft parts function
lib.fft_part.restype = None	
lib.fft_part.argtypes = [np.ctypeslib.ndpointer( flags="C"), ctypes.c_int, np.ctypeslib.ndpointer(flags="C"), ctypes.c_bool, ctypes.c_bool]



class c_complex(ctypes.Structure):
    # Complex number, compatible with std::complex layout
    _fields_ = [("real", ctypes.c_double), ("imag", ctypes.c_double)]

    def __init__(self, pycomplex):
        # Init from Python complex
        self.real = pycomplex.real
        self.imag = pycomplex.imag

    def to_complex(self):
        # Convert to Python complex
        return self.real + (1.j) * self.imag



def complex_check(l):
    if isinstance(l, np.ndarray) and l.dtype == np.complex and len(l.shape)==1:
        # the numpy array layout for complexes (sequence of two double) is already
        # compatible with std::complex 
        a = l.ctypes.data
    else:
        # otherwise, try to build our c_complex
        arr_t = c_complex * len(l)
        a = arr_t(*(c_complex(r) for r in l))
    b = np.copy(a)
    return b

def to_complex(arr):
    for element in arr:
        element = element[0] + 1j * element[1]
        print(element)
    return arr


def dft(signal):
    signal = complex_check(signal)
    output = np.copy(signal)
    lib.dft(signal, len(signal), output)
    # output = to_complex(output)
    return output

def rdft(signal):
    signal = complex_check(signal)
    output = np.empty((len(signal)),dtype=np.float64)
    lib.dft_part(signal, len(signal), output, 1 , 0)
    return output

def idft(signal):
    signal = complex_check(signal)
    output = np.empty((len(signal)),dtype=np.float64)
    lib.dft_part(signal, len(signal), output, 0 , 1)
    return output

def fft(signal):
    signal = complex_check(signal)
    output = np.copy(signal)
    lib.fft(output, len(output))
    return output

def rfft(signal):
    signal = complex_check(signal)
    output = np.empty((len(signal)),dtype=np.float64)
    lib.dft_part(signal, len(signal), output, 1, 0)
    return output

def ifft(signal):
    signal = complex_check(signal)
    output = np.empty((len(signal)),dtype=np.float64)
    lib.dft_part(signal, len(signal), output, 0 , 1)
    return output


# test = np.array([1. + 0.j, 0 + 1.j, 2 + 2.j, 2 + 1.j ])
# test2 = [1. + 0.j, 0 + 1.j, 2 + 2.j, 2 + 1.j ]

# b = complex_check(test2)
# print(b)
test2 = [1.5, 70.0, 81.0, 90.5, 0.0, 2.0, 15.7, 0.0]


f = np.fft.fft(test2)
print("np fft")
print(f)
# print(len(f))

print("dft")
df = dft(test2)
print(df)

# to_complex(df)
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