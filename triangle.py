from sympy import *
A = (int(input("xa: ")), int(input("ya: ")))
B = (int(input("xb: ")), int(input("yb: ")))
C = (int(input("xc: ")), int(input("yc: ")))
x, y = symbols('x y')
point = input("Point a b ou c ? ")
if point == "a":
    BC = (C[0]-B[0], C[1]-B[1])
    AM = (simplify(x-A[0]), simplify(y-A[1]))
    eq = simplify(AM[0]*BC[0]+AM[1]*BC[1])

elif point == "b":
    AC = (C[0]-A[0], C[1]-A[1])
    BM = (simplify(x-B[0]), simplify(y-B[1]))
    eq = simplify(BM[0]*AC[0]+BM[1]*AC[1])

elif point == "c":
    AB = (B[0]-A[0], B[1]-A[1])
    CM = (simplify(x-C[0]), simplify(y-C[1]))
    eq = simplify(CM[0]*AB[0]+CM[1]*AB[1])

eq = str(eq).replace("*", "")
print(f"{eq} = 0")
