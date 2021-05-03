import matplotlib.pyplot as plt
import numpy as np
import time
import lib



test_signals = []
sizes = []
errors = []
time_fft=[]
time_dft=[]




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
    plt.figure(1)
    plt.plot(sizes, errors)
    

def plot_complexity():
    plt.figure(2)
    plt.plot(sizes, time_fft)
    #plt.plot(sizes, time_dft)
    plt.legend(["FFT", "DFT"])
    plt.show()




def main():
    sample_signals(13)

    for signal in test_signals:
        start = time.time()
        fft = lib.fft(signal)
        end = time.time()
        time_fft.append(end-start)

        start = time.time()
        dft = lib.dft(signal)
        end = time.time()
        time_dft.append(end-start)

        calculate_errors(fft, dft)
        print("+")

    plot_errors()
    plot_complexity()



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