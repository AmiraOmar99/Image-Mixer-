import matplotlib.pyplot as plt
import numpy as np
import time
import lib

test_signals = []
sizes = []
errors = []
time_fft=[]
time_fft_amp=[]
time_dft=[]




def sample_signals(n):
    for i in range(n):
        sizes.append(2**(i+1))
        test_signals.append(np.random.rand(sizes[i],))


def calculate_errors(arr1,arr2):
    mse = np.square(arr1.view('complex') - arr2.view('complex')).mean()
    errors.append(np.abs(mse))


def plot_errors():
    plt.figure(1)
    plt.ylabel("mse")
    plt.xlabel("size of sample 'N'")
    plt.plot(sizes, errors)





def plot_complexity():
    plt.figure(2)
    plt.plot(sizes, time_fft_amp)

    plt.ylabel("time")
    plt.xlabel("size of sample 'N'")
    plt.plot(sizes, time_dft)
    plt.legend(["FFT_amp", "DFT"])
    

def plot_amp():
    plt.figure(3)
    plt.plot(sizes, time_fft)

    plt.ylabel("time")
    plt.xlabel("size of sample 'N'")
    plt.plot(sizes, time_dft)
    plt.legend(["FFT", "DFT"])
    plt.show()


def main():
    sample_signals(12)

    for signal in test_signals:
        start = time.time()
        fft = lib.fft(signal)
        end = time.time()
        time_fft.append(end-start)
        time_fft_amp.append(100*(end-start))

        start = time.time()
        dft = lib.dft(signal)
        end = time.time()
        time_dft.append(end-start)

        calculate_errors(fft, dft)
        print("+")

    plot_errors()
    plot_complexity()
    plot_amp()



if __name__ == '__main__':
    main()