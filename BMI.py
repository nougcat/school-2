# liczy BMI
def licz_BMI():
    weight= float(input("podaj swoją wagę w kg: "))
    height= float(input("podaj wzrost w metrach: "))
    bmi= weight / height  ** 2
    return bmi


dane = licz_BMI()

if dane > 0:
    print("BMI: ", dane)
if dane < 0:
    print("niepoprawne BMI")
    licz_BMI()

if dane < 18.5:
    print("masz niedowagę")
elif dane >= 18.5 and dane < 25:
    print("twoja masa jest prawidłowa")
else:
    print("masz nadwagę")