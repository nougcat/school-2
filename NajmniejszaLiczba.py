liczby = []
ile_razy = 3
for i in range(ile_razy):
    liczby.append(int(input(f"\nPodaj {i+1} liczbę: ")))

print(liczby)
najmniejsza = liczby[0]
for i in range(ile_razy):
    if najmniejsza>liczby[i]:
        najmniejsza=liczby[i]


print("najmniejszą liczbą jest:", najmniejsza)
