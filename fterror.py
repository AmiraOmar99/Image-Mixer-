import numpy as np
import lib





test2 = [1.5, 70.0, 81.0, 90.5, 0.0, 2.0, 15.7, 0.0]


f = np.fft.fft(test2)
print("np fft")
print(f)
# print(len(f))

print("dft")
df = lib.dft(test2)
print(df)

print("real")
rdf = lib.rdft(test2)
print(rdf)


print("imag")
idf = lib.idft(test2)
print(idf)



print("fft")
df = lib.fft(test2)
print(df)

print("real")
rdf = lib.rfft(test2)
print(rdf)


print("imag")
idf = lib.ifft(test2)
print(idf)