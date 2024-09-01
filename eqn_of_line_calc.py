import sympy as sp
from sympy import Symbol


# Define your function below
def linear(a, b, c, d):
    y = Symbol("y")
    x = Symbol("x")
    # find slope
    slope = (d - b) / (c - a)
    # point slope form
    eqn1 = sp.Eq(y - b, slope * (x - a))
    # linear form
    eqn2 = sp.solve(eqn1, y)[0]

    return eqn2
