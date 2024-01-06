text = input("Podaj tekst do anonimizacji: ")

final_text = ""

for char in text:
    if char.isdigit():
        final_text += "X"
    else:
        final_text += char

print("Zanonimizowany tekst to", final_text)
