import matplotlib.pyplot as plt
import numpy as np
import lib


test_signals = []
sizes = []
errors = []
time=[]


def sample_signals(n):
    for i in range(n):
        sizes.append(2**(i+1))
        test_signals.append(np.random.rand(sizes[i],))

# def sample_signals():
#     sizes.append(2**13)
#     test_signals.append(np.random.rand(2**13,))

def calculate_errors(arr1,arr2):
    mse = np.square(arr1.view('complex') - arr2.view('complex')).mean()
    errors.append(np.abs(mse))

def plot_errors():
    plt.plot(sizes, errors)
    plt.show()

def plot_complexity():




def main():
    sample_signals(10)

    # fft = np.fft.fft(test_signals[0])
    # #print(fft)
    # dft = lib.dft(test_signals[0])
    # #print(dft)
    # # calculate_errors(fft, np.array(dft , dtype=np.complex128))
    # calculate_errors(fft, dft)

    for signal in test_signals:
        fft = np.fft.fft(signal)
        #print(fft)
        dft = lib.dft(signal)
        #print(dft)
        # calculate_errors(fft, np.array(dft , dtype=np.complex128))
        calculate_errors(fft, dft)
        print("+")

    plot_errors()




    # f = np.fft.fft(test_signals[0])
    # print("np fft")
    # print(f)

    # df = lib.dft(test_signals[0])
    # print("dft")
    # print(df)

    # print("real")
    # rdf = lib.rdft(test_signals[0])
    # print(rdf)


    # print("imag")
    # idf = lib.idft(test_signals[0])
    # print(idf)

    # print("fft")
    # df = lib.fft(test_signals[0])
    # print(df)

    # print("real")
    # rdf = lib.rfft(test_signals[0])
    # print(rdf)

    # print("imag")
    # idf = lib.ifft(test_signals[0])
    # print(idf)



if __name__ == '__main__':
    main()