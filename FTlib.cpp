#include <iostream>
#include <vector>
#include <complex>
#include <cmath>


extern "C"
{
       
    class dft
    {
    // methods
    public:
        // constructor
        dft(std::vector<double> input_signal){
            signal = input_signal;
            N = signal.size();
            construct_mat();
            get_components();
        }

    private:
        void construct_mat() {

            freq_matrix.resize(N, std::vector<std::complex<double>>(N));
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
        }

        void get_components() {

            ft.resize(N);
            rft.resize(N);
            ift.resize(N);
            
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    ft[i] = ft[i] + (signal[i] * freq_matrix[i][j]);
                }
                rft[i] = ft[i].real();
                ift[i] = ft[i].imag();
            }
        }
        
    // members
    public:
        std::vector<std::complex<double>> ft;
        std::vector<double> rft;
        std::vector<double> ift;

    private:
        int N;
        std::vector<std::vector<std::complex<double>>>freq_matrix;
        std::vector<double> signal;
    };

}


int main(){
    int size = 10;
    std::vector<double> signal(size, 1);
    auto s = dft(signal);
    
    for (int i = 0; i < size; i++) {
        std::cout << s.ft[i] << std::endl;
    }
    std::cout << s.rft[1] << std::endl;
    std::cout << s.ift[1] << std::endl;
    
    return 0;
}