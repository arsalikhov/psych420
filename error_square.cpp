#include <iostream>
#include <cmath>

using namespace std;

double Nth_root(double resultant){  // Function to determine Nth root of a number

    double base; // The answer to the problem

    double exp;
    exp = 2;

    base = pow(resultant, 1/exp); // Formula to determine the base of a exponent and a resultant

    

    // cout << resultant << "^" << "2" << exp << " = " << base << endl;

    return base;

}

void error(double guess, double resultant){

    double error_value, base;
    base = Nth_root(resultant);
    error_value = guess*2 - base;

    cout << error_value;

}

int main (){  // Global main function

    error(3.9, 16);
    return 0;
}
