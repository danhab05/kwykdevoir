from sympy import *
x, y = symbols('x y')

u = (int(input("xu: ")), int(input("yu: ")))
A = (int(input("xa: ")), int(input("ya: ")))
n = (u[1], -1*u[0])
AM = (simplify(x-A[0]), simplify(y-A[1]))

print(simplify(AM[0]*n[0]+AM[1]*n[1]))


print("=0")
