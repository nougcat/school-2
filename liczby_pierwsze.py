from math import sqrt


def test(sprawdzana_liczba):

    if sprawdzana_liczba > 2 and sprawdzana_liczba % 2 == 0:
        return False
    if sprawdzana_liczba > 3 and sprawdzana_liczba % 3 == 0:
        return False
    if sprawdzana_liczba > 5 and sprawdzana_liczba % 5 == 0:
        return False
    if sprawdzana_liczba > 7 and sprawdzana_liczba % 7 == 0:
        return False

    for i in range(1, int(sqrt(sprawdzana_liczba)+1)):
        if sprawdzana_liczba%i == 0: 
            print(sprawdzana_liczba, end=' ')
            return True

x=0
sprawdzana_liczba = 2
print('pierwsze 30 liczb pierwszych to: ',end='')

while x!=30:
    a = test(sprawdzana_liczba)
    if a == True: x +=1
    sprawdzana_liczba += 1
    
        
print("")