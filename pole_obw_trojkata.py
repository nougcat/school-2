from math import sqrt

# Upiększanie danych
def cleanVar(a):
    if float(a) == int(a):
        return int(a)
    else:
        return a


# Wprowadzenie danych oraz przeciw prostokątna
a = float(input("Podaj dlugosc pierwszej przyprostokatnej"))
b = float(input("Podaj dlugosc drugiej przyprostokatnej"))
a = cleanVar(a)
b = cleanVar(b)
c = sqrt(a**2+b**2)

print("Dla trojkata prostokatnego o dlugosciach przyprostokatnych", a, "i", b,":")
print("pole wynosi:", cleanVar(a*b/2))
print("obwod wynosi:", cleanVar(a+b+c))