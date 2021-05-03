import ctypes
import numpy as np


lib = ctypes.CDLL('./lib.so')

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

lib.dft.restype = None	
# lib.dft.argtypes = [np.ctypeslib.ndpointer(np.complex, flags="C_CONTIGUOUS"), ctypes.c_int, np.ctypeslib.ndpointer(np.complex, flags="C_CONTIGUOUS")]
# lib.dft.argtypes = [np.ctypeslib.ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"), ctypes.c_int, np.ctypeslib.ndpointer(ctypes.c_double, flags="C_CONTIGUOUS")]
lib.dft.argtypes = [np.ctypeslib.ndpointer( flags="C_CONTIGUOUS"), ctypes.c_int, np.ctypeslib.ndpointer(flags="C_CONTIGUOUS")]


def dft(l):
    if isinstance(l, np.ndarray) and l.dtype == np.complex and len(l.shape)==1:
        # the numpy array layout for complexes (sequence of two double) is already
        # compatible with std::complex (see https://stackoverflow.com/a/5020268/214671)
        a = l.ctypes.data
        # print(a, "kk")
    else:
        # otherwise, try to build our c_complex
        arr_t = c_complex * len(l)
        a = arr_t(*(c_complex(r) for r in l))
        # print(a, "nnn")
    b = np.copy(a)
    a = np.copy(b)
    # print(a.dtype, "  ", b.dtype)
    # print(b, "l")
    # print(a, "ok@")
    lib.dft(a, len(l), b)
    # for element in b:
        # element = element.to_complex
    return b


test = np.array([1. + 0.j, 0 + 1.j, 2 + 2.j, 2 + 1.j ])
# test2 = [1. + 0.j, 0 + 1.j, 2 + 2.j, 2 + 1.j ]
test2 = [1.5, 70.0, 81.0, 90.5, 0.0, 2.0, 15.7, 0.0]


f = np.fft.fft(test2)
print("np fft")
print(f)
print(len(f))

print("dft")
# dft(test2)
df = dft(test2)
print(df)
print(len(df))


_sum_it_cplx = lib.sum_it_cplx
_sum_it_cplx.restype = c_complex

def sum_it_cplx(l):
    if isinstance(l, np.ndarray) and l.dtype == np.complex and len(l.shape)==1:
        # the numpy array layout for complexes (sequence of two double) is already
        # compatible with std::complex (see https://stackoverflow.com/a/5020268/214671)
        a = l.ctypes.data
    else:
        # otherwise, try to build our c_complex
        arr_t = c_complex * len(l)
        a = arr_t(*(c_complex(r) for r in l))
    ret = _sum_it_cplx(a, len(l))
    return ret.to_complex()

# from a complex list (with copy)
# print(sum_it_cplx([1. + 0.j, 0 + 1.j, 2 + 2.j]))
# from a numpy array of the right type - zero-copy
# print(sum_it_cplx(np.array([1. + 0.j, 0 + 1.j, 2 + 2.j])))