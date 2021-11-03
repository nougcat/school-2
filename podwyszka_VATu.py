print("Cena po nowym VATcie \n")

kwota = float(input("Cena produktu:"))
staryVat = float(input("Stary VAT:"))
nowyVat = float(input("Nowy VAT:"))


# liczenie ceny brutto
netto = kwota / (1 + staryVat / 100)
print("\n \nCena netto:", round(netto, 2), "pln")

# nowa cena
nowaCena = netto + netto * (nowyVat / 100)
print("Nowa cena:", round(nowaCena, 2), "pln")
