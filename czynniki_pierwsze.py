print("Ten program sprawdza wszystkie czynniki pierwsze dla wszystkich liczb naturalych od 2")
a = int(input('podaj liczbe: '))
x=a
print('czynniki',a,'to ', end='')
liczbaCzynnikow = 0

# Sprawdzamy czy liczba dzieli się przez liczby od dwóch do połowy swojej wartości
for i in range(2,int(a/2)+1):
    while a%i == 0:
        a = a/i
        print(int(i),end=' ')
        liczbaCzynnikow +=1

if a == x: 
    print(x)
    liczbaCzynnikow +=1
print('\nliczba czynników = ',liczbaCzynnikow)