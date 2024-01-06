text = input("Wpisz tekst do sprawdzenia: ")

open_counter = 0
close_counter = 0

for char in text:
    if char == "(":
        open_counter += 1
    if char == ")":
        close_counter += 1

if open_counter == close_counter:
    print("Tekst jest ok")
elif open_counter > close_counter:
    print("Za mało nawiasów zamykających")
else:
    print("Za mało nawiasów otwierających")