from sympy import *


def mediatrice():
    A = (int(input("xa: ")), int(input("ya: ")))
    B = (int(input("xb: ")), int(input("yb: ")))
    x, y = symbols('x y')
    AB = (B[0]-A[0], B[1]-A[1])
    I = ((A[0]+B[0])/2, (A[1]+B[1])/2)
    IM = (simplify(x-I[0]), simplify(y-I[1]))
    eq = simplify(AB[0]*IM[0]+AB[1]*IM[1])
    eq = str(eq).replace("*", "")
    print(f"L'equation est: {eq} = 0")


def diametre():
    x, y = symbols('x y')
    A = (int(input("xa: ")), int(input("ya: ")))
    B = (int(input("xb: ")), int(input("yb: ")))
    I = ((A[0]+B[0])/2, (A[1]+B[1])/2)
    AB = (B[0]-A[0], B[1]-A[1])
    rayon = sqrt(AB[0]**2+AB[1]**2) / 2
    IM = (simplify(x-I[0]), simplify(y-I[1]))
    print("L'equation est: (" + str(IM[0]) + ")**2 " +
          "+ (" + str(IM[1]) + ")**2" + " = " + str(rayon**2))


def triangle():
    A = (int(input("xa: ")), int(input("ya: ")))
    B = (int(input("xb: ")), int(input("yb: ")))
    C = (int(input("xc: ")), int(input("yc: ")))
    x, y = symbols('x y')
    point = input("Issue de quel point ? (a b ou c): ")
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
    print(f"L'equation est: {eq} = 0")


def vecteur():
    x, y = symbols('x y')
    u = (int(input("xu: ")), int(input("yu: ")))
    A = (int(input("xa: ")), int(input("ya: ")))
    n = (u[1], -1*u[0])
    AM = (simplify(x-A[0]), simplify(y-A[1]))

    eq = simplify(AM[0]*n[0]+AM[1]*n[1])

    eq = str(eq).replace("*", "")
    print(f"L'equation est: {eq} = 0")


def main():
    print("Quelle type d'exercie? \n1 Exercice avec le cercle ainsi que le diametre AB\n2 Exercice avec le triangle issue d'un point (a,b,c)\n3 Exercice Avec la mediatrice et le segment AB\n4 Exercice avec le vecteur u et le point a")
    n = input("Choix: ")
    if n == "1":
        diametre()
    elif n == "2":
        triangle()
    elif n == "3":
        mediatrice()
    elif n == "4":
        vecteur()


main()
