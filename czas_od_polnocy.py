print("ten program obliczy ile sekund minęło od północy")
print("Pod spodem wpisz dane: godzinę minutę i sekundę, aby potwierdzić wybór naciśnij enter")
hours = int(input("Podaj godzinę: "))
minutes = int(input("Podaj minutę: "))
seconds = int(input("Podaj sekundę: "))
print("aktualna godzina:")
print(hours, ":",minutes,":",seconds)
sinceNoon = seconds + minutes * 60 + hours * 3600

print("Od północy minęło ", sinceNoon, "sekund")