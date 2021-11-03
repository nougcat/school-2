import random

random.seed()


def gra():
    a = -5
    rand = random.randrange(0, 100)
    while 1:
        a = int(input("podaj liczbe od 0 do 100: "))

        if rand == a:
            print("dobra odpowiedź, chcesz grać ponownie?: ")
            ans = input('napisz "tak" jesli chcesz grać ponownie:\n')
            if ans.upper() == "TAK":
                gra()
            else:
                break

        elif a > rand:
            print("dana liczba jest większa od docelowej")
        else:
            print("dana liczba jest mniejsza od docelowej")


gra()