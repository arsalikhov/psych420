from sympy import Derivative
from sympy import *
import numpy as np


def t_power_n(t, n):
    """Computes t to the power of n

    Args:
        t ([float]): base of the equation
        n ([int]): exponent value
    """       
    f_to_n = float(t**n)
    return f_to_n

def diff_t_power_n(t, n):
    """Computes derivative of t_power_n function

    Args:
        t ([float]): base of the equation
        n ([int]): exponent value
    """       
  
    x = symbols('x')
    f = x**n
    d = diff(f, x).doit()

    string_derivative = str(d).replace('*x**', ' ')
    a_and_b = [float(s) for s in string_derivative.split() if s.isdigit()]

    a = a_and_b[0]
    b = a_and_b[1]

    diff_f_to_n = float(a*t**b)
    return diff_f_to_n
    
def get_step(initial_guess, goal, n):
    """computes the step error between initial guess and the right answer

    Args:
        initial_guess ([float or int]): initial guess for the values of nth root
        goal ([float or int]): the resultant of the correct guess to the power of n
        n ([int]): exponent value

    """    
    step = ((goal - t_power_n(initial_guess, n))
    /(diff_t_power_n(initial_guess, n)))
    return step



def get_nth_root(goal, initial_guess, n, tolerance = 4):
    """itirates over multiple intermidiate guesses for nth root to find the closest one 

    Args:
        initial_guess ([float or int]): initial guess for the values of nth root
        goal ([float or int]): the resultant of the correct guess to the power of n
        n ([int]): exponent value
        tolerance (int, optional): number of decimals the function approximates to. Defaults to 4.
    """    
    guess = initial_guess + get_step(initial_guess, goal, n)
    print(f'New guess is %s' %(guess))
    if round(guess**n, tolerance) != goal:
        new_guess = guess
        get_nth_root(goal, new_guess, n)

    
        
get_nth_root(16, 5, 4)
