#Kent Tran
import sympy as sp
from sympy import symbols, limit, oo, log, simplify

n = symbols('n', positive=True, real=True)

def same_asymptotic(left_func, right_func):
    left = sp.sympify(left_func)
    right = sp.sympify(right_func)

    if left == 0 or right == 0:
        return left == right
        
    ratio1 = limit(left / right, n, oo)
    ratio2 = limit(right / left, n, oo)

    is_ratio1_valid = (ratio1.is_finite and ratio1.is_positive and ratio1 != 0)
    is_ratio2_valid = (ratio2.is_finite and ratio2.is_positive and ratio2 != 0)

    return is_ratio1_valid and is_ratio2_valid
