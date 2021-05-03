#include <iostream>
#include <vector>
#include <complex>
#include <cmath>



extern "C" {




const double PI = 3.141592653589793238460;

typedef std::complex<double> Complex;
typedef std::valarray<Complex> CArray;


std::complex<double> sum_it_cplx(std::complex<double> *array, int size) {
    std::complex<double> ret(0., 0.);
    for(int i=0; i<size; ++i) {
        ret += array[i];
    }
    return ret;
}


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

    
void dft(std::complex<double> signal[], int size, std::complex<double> output[])
{
    std::complex<double>* signal_dft = (std::complex<double>*) malloc(size * sizeof(std::complex<double>)); 

    std::vector<std::vector<std::complex<double>>>freq_mat = construct_mat(size);

    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            signal_dft[i] = signal_dft[i] + (signal[j] * freq_mat[i][j]);
        }
        output[i] = signal_dft[i];
    }

}


// Cooley–Tukey FFT (in-place)
void fft2(Complex x[], int N) 
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
	fft2(even, N/2);
	fft2(odd, N/2 + (N%2));

	// combine
	for (size_t k = 0; k < N/2; ++k)
	{
		Complex t = std::polar(1.0, -2 * PI * k / N) * odd[k];
		x[k    ] = even[k] + t;
		x[k+N/2] = even[k] - t;
	}
}



}