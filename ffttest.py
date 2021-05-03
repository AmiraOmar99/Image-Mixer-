import numpy as np


test = np.array([1.5, 70.0, 81.0, 90.5, 0.0, 2.0, 15.7, 0.0])

out  = np.fft.fft(test)

print(out[1])