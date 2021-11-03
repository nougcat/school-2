print("program do sprawdzania czy coś jest trójkątem oraz czy jest on prostokątny")
a = float(input("podaj a: "))
b = float(input("podaj b: "))
c = float(input("podaj c: "))

if a + b > c and b + c > a and a + c > b:
    print("to jest trójkąt i ")
else:
    print("to nie jest trójkąt i ")

if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + b ** 2 == c ** 2:
    print("jest to trójkąt jest prostokątny oraz ")
else:
    print("nie jest to trójkąt prostokątny oraz ")

if a == b and b == c:
    print("jest to trójkąt równoboczny")
else:
    print("nie jest to trójkąt równoboczny")