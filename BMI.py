growth = float(input("Podaj swój wzrost w cm: "))/100
weight = float(input("Podaj swoją wagę w kg: "))

bmi = weight / (growth * growth)

if bmi < 18.5:
    print("Ważysz za mało")
elif bmi < 25:
    print("Twoja waga jest w normie")
elif bmi < 30:
    print("Masz nadwagę")
else:
    print("Cierpisz na otyłość")        