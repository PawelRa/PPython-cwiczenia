text = input("Wpisz tekst do sprawdzenia: ")
words = len(text.split(' '))

all_letters = len(text) - words + 1
division = all_letters / words

print("Słowa w Twoim tekście mają średnio ", division, "znaków.")