liczby=[]
liczby_dwucyfrowe=0

y = int(input("Ile liczb chcesz wprowadzić?: "))
for x in range(y):
    # Dodajemy liczbe do listy
    liczby.append(int(input(f"podaj {x+1} liczbe: ")))
    
    # Sprawdzamy czy jest dwucyfrowa
    if liczby[x]>= 10 and liczby[x]<=99:
        liczby_dwucyfrowe +=1

print("Liczb dwucyfrowych jest:",liczby_dwucyfrowe)
