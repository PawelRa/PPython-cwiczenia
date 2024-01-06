text = input("Podaj tekst do anonimizacji: ")

for digit in "0123456789":
    text = text.replace(digit,"X")

print("Zanonimizowany tekst to", text)