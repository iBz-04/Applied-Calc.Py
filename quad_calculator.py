#QUADRATIC EQ CALCULATOR
from numpy import sqrt
from sympy.plotting import *
from sympy import Symbol

#ax^2 + bx + c

def zeros(a, b, c):
    D = sqrt(b*b - 4*a*c)
    x1 = (-b + D)/(2*a)
    x2 = (-b - D)/(2*a)

    print("The first root is: ", x1)
    print("The second root is: ", x2)

def printGraph(a, b, c):
    x = Symbol("x")
    plot(a*x**2 + b*x + c)
    
if __name__ == "__main__":
    while True:
        print("welcome to the quad calculator")
        a = input("Enter a: ")
        b = input("Enter b: ")
        c = input("Enter c: ")
        zeros(float(a), float(b), float(c))
        printGraph(float(a), float(b), float(c))

        allDone = input("would you like to solve another quadratic? (y/n)")
        if allDone == "n":
            print("Goodbye")
            break
        
