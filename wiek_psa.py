print("Kalkulator wieku psa")
age = int(input("Podaj wiek psa: "))

if age > 0 and age <= 2:
    print("Wiek Twojego psa wynosi",10.5 * age)
else:
    print("Wiek Twojego psa wynosi", 4 * (age - 2) + 21)