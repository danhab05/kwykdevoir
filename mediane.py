from sympy import *
A = (int(input("xa: ")), int(input("ya: ")))
B = (int(input("xb: ")), int(input("yb: ")))
x, y = symbols('x y')
AB = (B[0]-A[0], B[1]-A[1])
print(AB)
I = ((A[0]+B[0])/2, (A[1]+B[1])/2)
print(I)
IM = (simplify(x-I[0]), simplify(y-I[1]))
eq  = simplify(AB[0]*IM[0]+AB[1]*IM[1])
eq = str(eq).replace("*", "")
print(f"{eq} = 0")
