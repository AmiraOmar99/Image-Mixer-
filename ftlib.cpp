#include <iostream>
#include <vector>
#include <complex>
#include <cmath>
#include <valarray>

extern "C"
{

const double PI = 3.141592653589793238460;

typedef std::complex<double> Complex;
typedef std::valarray<Complex> CArray;


// construct the frequency matrix
std::vector<std::vector<std::complex<double>>> construct_mat(int N) {
    std::vector<std::vector<std::complex<double>>> freq_matrix(N, std::vector<std::complex<double>>(N));

    std::complex<double> i;
    double pi = 2 * asin(1);
    i = -1;
    i = sqrt(i);
    std::complex<double> w = exp((-2 * pi / N) * i);

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            freq_matrix[i][j] = pow(w, ((i) * (j)));
        }
    }
    return freq_matrix;
}


// dft using the freq matrix    
void dft(std::complex<double> signal[], int size, std::complex<double> signal_dft[])
{
    std::vector<std::vector<std::complex<double>>>freq_mat = construct_mat(size);

    for (int i = 0; i < size; i++) {
        signal_dft[i] = 0;
        for (int j = 0; j < size; j++) {
            signal_dft[i] = signal_dft[i] + (signal[j] * freq_mat[i][j]);
        }
    }

}

void dft_real(std::complex<double> signal[], int size, std::complex<double> output[])
{
    std::complex<double> signal_dft[size];
    dft(signal, size, signal_dft);
    for(int i = 0; i < size; i++)
    {
        output[i] = signal_dft[i].real();
    }
}


void dft_imag(std::complex<double> signal[], int size, double output[])
{
    std::complex<double> signal_dft[size];
    dft(signal, size, signal_dft);
    for(int i = 0; i < size; i++)
    { 
        output[i] = signal_dft[i].imag();
        
    }
}


// Cooley–Tukey FFT (in-place)
void fft(Complex x[], int N) 
{
	// const size_t N = x.size();
	if (N <= 1) return;

	// divide
    Complex even[N/2]; 
    Complex odd[N/2 + (N%2)];
    for (int i = 0; i < N; i++)
    {
        if(i % 2 == 0)
        {
            even[i/2] = x[i];
        }
        else
        {
            odd[(i-1)/2] = x[i];
        }
    } 

	// conquer
	fft(even, N/2);
	fft(odd, N/2 + (N%2));

	// combine
	for (size_t k = 0; k < N/2; ++k)
	{
		Complex t = std::polar(1.0, -2 * PI * k / N) * odd[k];
		x[k    ] = even[k] + t;
		x[k+N/2] = even[k] - t;
	}

}


void fft_real (Complex x[], int N, double output[])
{  
   fft(x,N);
   for (int i = 0; i < N; i++)
	{   
        output[i] = x[i].real();
	}
}

void fft_imag (Complex x[], int N, double output[])
{  
   fft(x,N);
   for (int i = 0; i < N; i++)
	{   
		output[i] = x[i].imag();

	}
}



}