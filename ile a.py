text = input("Wpisz tekst do sprawdzenia: ")

counter = 0
for char in text:
    if char.lower() == "a":
        counter += 1

print("Litera a wystąpiła", counter, "razy")