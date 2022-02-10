#include <iostream>
#include <cmath>

using namespace std;

double derivative(double x, double h, double n){
    
    double answer;
    answer = operator(([pow((x + h), 1/n) - pow(x - h, 1/n)) / 2 * h);

    cout << answer

}


int main (){  // Global main function

    derivative(27, 5, 3);
    return 0;

}




