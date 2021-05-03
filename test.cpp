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


void dft2(std::complex<double> signal[], int size, std::complex<double> output[])
{
    for (int i = 0; i < size; i++) {
        std::complex<double> xi (0,0);
        for (int j = 0; j < size; j++) 
        {
            double realpart = cos(((2*PI)/size)*i*j);
            double imagpart = sin(((2*PI)/size)*i*j);
            std::complex<double> w (realpart,-imagpart);
            xi += signal[j] * w;        
        }
        output[i] = xi;
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



int main()
{
    // Complex test[] = {1.5, 70.0, 81.0, 90.5, 0.0, 2.0, 15.7, 0.0 };
    // CArray out1(test, 8);
	// fft(out1); //complex_numbers

    // Complex test2[] = {1.5, 70.0, 81.0, 90.5, 0.0, 2.0, 15.7, 0.0 };
    // fft2(test2, 8);

    // int N = 1024;
    // double Ts = 1.0/N;
    // double t[10241];
    // double x[10241];
    // double y[10241];
    // Complex W [10241];
    // for(int i = 0; i < 10241; i++)
    // {
    //     t[i] = i * Ts;
    //     x[i] = 1 * cos(2*PI*500*t[i]);
    //     y[i] = 0 * sin(2*PI*3*t[i]);
    //     W[i] = std::complex<double> (x[i],-y[i]);
    // }
    // Complex out[10241];
    // dft(W,10241,out);

    // std::cout << (1.0/N) *out[500]<< std::endl;

    // for(int i = 0; i < 10241;i++)
        // std::cout << out[i] << std::endl;

    // std::cout << data[1] << std::endl;
    std::complex<double> signal[] = {1.5, 70.0, 81.0, 90.5, 0.0, 2.0, 15.7, 0.0};

    std::complex<double> out[] = {1,1,1,1,1,1,1,1};

    dft(signal,8, out);

    // std::complex<double> signal[]={ 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0 };
    // std::complex<double> out[] = {1,1,1,1,1,1,1,1};
    // std::complex<double> out1[8];
    // std::complex<double> out2[8];

    // dft2(signal,8, out2);




    for(int i = 0; i < 8; i++)
    {
        std::cout << out[i] << std::endl;

    //     std::cout << out1[i] << std::endl;
    //     std::cout << test2[i] << std::endl;
    }



//     double* real = dft_real(signal,10);
//     double* imag = dft_imag(signal,10);
// // 
//     std::cout << real[1] << std::endl;
    // std::cout << imag[1] << std::endl;  

    // std::cout << real[5] << std::endl;
    // std::cout << imag[5] << std::endl;


    // const Complex test[] = {1.5, 70.0, 81.0, 90.5, 0.0, 2.0, 15.7, 0.0 };
    // CArray data(test, 8);
	// fft(data); //complex_numbers

    // std::cout << data[1] << std::endl;


}
}