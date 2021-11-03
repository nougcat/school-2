liczba = int(input("Podaj liczbe: "))
wiersz=1
while wiersz <= liczba:
    #Pierwsza literacja
    #                od 1,                 do liczba+1       1++
    for x in range((wiersz-1)*liczba + 1, wiersz*liczba + 1, 1):
        print(x, end=' ')
    
    if wiersz!=liczba: print("\n")
    wiersz+=1
