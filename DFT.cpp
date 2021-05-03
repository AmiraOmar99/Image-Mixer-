#include <iostream>
#include <vector>
#include <complex>
#include <cmath>


std::vector<std::vector<std::complex<double>>> construct_mat(int N) {
    std::vector<std::vector<std::complex<double>>> freq_matrix(N, std::vector<std::complex<double>>(N));

    std::complex<double> i;
    double pi = 2 * asin(1);
    i = -1;
    i = sqrt(i);
    std::complex<double> w = exp(-2 * pi / N * i);
    // std::cout << w << std::endl;

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




std::vector<double> dft_real(std::vector<double> signal)
{
    int N = signal.size();
    std::vector<std::complex<double>> complex_dft = dft(signal);
    std::vector<double> real_dft(N);

    for (int i = 0; i < N; i++) {
        real_dft[i] = complex_dft[i].real(); 
    }
    return real_dft;
}

std::vector<double> dft_imag(std::vector<double> signal)
{
    int N = signal.size();
    std::vector<std::complex<double>> complex_dft = dft(signal);
    std::vector<double> imag_dft(N);

    for (int i = 0; i < N; i++) {
        imag_dft[i] = complex_dft[i].imag();
    }
    return imag_dft;

}


std::vector<double> dft_magnitude(std::vector<double> signal)
{
    int N = signal.size();
    std::vector<std::complex<double>> complex_dft = dft(signal);
    std::vector<double> mag_dft(N);

    for (int i = 0; i < N; i++) {
        double real_part = complex_dft[i].real();
        double imag_part = complex_dft[i].imag();
        mag_dft[i] = sqrt(pow(real_part, 2) + pow(imag_part, 2));
    }
    return mag_dft;

}


std::vector<double> dft_phase(std::vector<double> signal)
{
    int N = signal.size();
    std::vector<std::complex<double>> complex_dft = dft(signal);
    std::vector<double> phase_dft(N);

    for (int i = 0; i < N; i++) {
        double real_part = complex_dft[i].real();
        double imag_part = complex_dft[i].imag();
        phase_dft[i] = atan(imag_part/real_part);
    }
    return phase_dft;

}




//test
int main()
{
    int size = 10;
    std::vector<double> signal(size, 1);
    std::vector<std::complex<double>> complex_dft = dft(signal);
    
    //print complex dft output
    // for (int i = 0; i < size; i++) {
        // std::cout << complex_dft[i] << std::endl;
    // }

    std::cout << complex_dft[1] << std::endl;

    std::vector<double> real = dft_real(signal);
    std::vector<double> imag = dft_imag(signal);

    std::cout << real[1] << std::endl;
    std::cout << imag[1] << std::endl;

    std::cout << real[5] << std::endl;
    std::cout << imag[5] << std::endl;

    // // std::vector<double> abs = dft_magnitude(signal);
    // // std::vector<double> angle = dft_phase(signal);
    
    // std::cout << abs[1] << std::endl;
    // std::cout << angle[1] << std::endl;

	
	
}

