from sympy import *
x, y = symbols('x y')

A = (int(input("xa: ")), int(input("ya: ")))
B = (int(input("xb: ")), int(input("yb: ")))
I = ((A[0]+B[0])/2, (A[1]+B[1])/2)


AB = (B[0]-A[0], B[1]-A[1])
rayon = sqrt(AB[0]**2+AB[1]**2) / 2

IM = (simplify(x-I[0]), simplify(y-I[1]))


print("(" + str(IM[0]) + ")**2 " +
      "+ (" + str(IM[1]) + ")**2" + " = " + str(rayon**2))
