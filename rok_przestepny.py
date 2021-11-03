from calendar import isleap

rok = int(input("podaj rok: "))

print(isleap(rok))

## "legalny" sposób

if rok % 4 == 0:
    if rok % 100 != 0 or rok % 400 == 0:
        print("Rok jest przestępny")
    else:
        print("Rok nie jest przestępny")
else:
    print("Rok nie jest przestępny")