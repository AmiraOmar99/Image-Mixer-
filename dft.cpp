// #include <stdio.h>
// #include <complex.h>
// #include <math.h>
#include <iostream>
#include <complex>
#include <cmath>


extern "C"
{
std::complex<double>** construct_mat(int const size)
{
    
    // std::complex<double>freq_matrix[size][size];
    std::complex<double>** freq_matrix = (std::complex<double> **) malloc(sizeof(std::complex<double> *) * size);
    for(int i = 0; i < size; i++)
    {
        freq_matrix[i] = (std::complex<double>  *) malloc(size * sizeof(std::complex<double>));
    }

    std::complex<double> i;
    double pi = 2 * asin(1);
    i = -1;
    i = sqrt(i);
    std::complex<double> w = exp(-2 * pi / size * i);
    // std::cout << w << std::endl;

    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            freq_matrix[i][j] = pow(w, (i*j));
        }
    }
    return freq_matrix;
}


void print_mat(std::complex<double>** matrix,int N) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

std::complex<double>* dft(double* signal, int size)
{
    std::complex<double>* signal_dft = (std::complex<double>*) malloc(size * sizeof(std::complex<double>)); 
    std::complex<double>** freq_mat = construct_mat(size);


    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            signal_dft[i] = signal_dft[i] + (signal[i] * freq_mat[i][j]);
        }
    }

    // free(*freq_mat);
    // free(freq_mat);
    return signal_dft;
}

double * dft_real(double* signal,int size)
{
    std::complex<double>* complex_dft = dft(signal, size);
    double* real_dft = (double *) malloc(size * sizeof(double)); 

    for(int i = 0; i < size; i++)
    {
        real_dft[i] = complex_dft[i].real();
    }

    // free(complex_dft);
    return real_dft;
}

double * dft_imag(double* signal,int size)
{
    std::complex<double>* complex_dft = dft(signal, size);
    double* imag_dft = (double *) malloc(size * sizeof(double)); 

    for(int i = 0; i < size; i++)
    {
        imag_dft[i] = complex_dft[i].imag();
    }

    // free(complex_dft);
    return imag_dft;
}
}


int main()
{
    double signal[] = {1,1,1,1,1,1,1,1,1,1};

    std::complex<double>* complex_dft = dft(signal,10);
    std::cout << complex_dft[1] << std::endl;

    double* real = dft_real(signal,10);
    double* imag = dft_imag(signal,10);

    std::cout << real[1] << std::endl;
    std::cout << imag[1] << std::endl;  

    std::cout << real[5] << std::endl;
    std::cout << imag[5] << std::endl;
}