#include <iostream>
#include <vector>
#include<complex>
#include <cmath>


std::vector<std::vector<std::complex<double>>> construct_mat(int N) {
    std::vector<std::vector<std::complex<double>>> freq_matrix(N, std::vector<std::complex<double>>(N));

    std::complex<double> i;
    double pi = 2 * asin(1);
    i = -1;
    i = sqrt(i);
    std::complex<double> w = exp(-2 * pi / N * i);

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            freq_matrix[i][j] = pow(w, ((i) * (j)));
        }
    }
    return freq_matrix;
}

void print_mat(std::vector<std::vector<std::complex<double>>> matrix,int N) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }
}


std::vector<std::complex<double>> dft(std::vector<double> signal) {
    int N = signal.size();
    std::vector<std::complex<double>> signal_dft(N, 0);
    std::vector<std::vector<std::complex<double>>>freq_matrix = construct_mat(N);

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            signal_dft[i] = signal_dft[i] + (signal[i] * freq_matrix[i][j]);
        }
    }
    return signal_dft;
}

//test
int main()
{
    int size = 10;
    std::vector<double> signal(size, 1);
    std::vector<std::complex<double>> complex_dft = dft(signal);
    
    //print complex dft output
    for (int i = 0; i < size; i++) {
        std::cout << complex_dft[i] << std::endl;
    }





	
	
}

