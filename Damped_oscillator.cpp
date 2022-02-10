#include <iostream>
#include <cmath>

using namespace std;

void Damped_oscillator(double resultant, double exp){  // Function to determine Nth root of a number

    double base; // The answer to the problem

    base = pow(resultant, 1/exp); // Formula to determine the base of a exponent and a resultant

    cout << resultant << "^" << "1/" << exp << " = " << base << endl;

}

int main (){  // Global main function

    Damped_oscillator(16, 2);
    return 0;

}
