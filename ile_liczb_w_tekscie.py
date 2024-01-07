PUNCTUATION_MARKS = ".,?!%$()"

raw_text = input("Wpisz tekst do sprawdzenia: ")

for mark in PUNCTUATION_MARKS:
    raw_text = raw_text.replace(mark, ' ')

words = raw_text.split()

how_many_numbers = 0
for word in words:
    if word.isnumeric():
        how_many_numbers += 1

result = (how_many_numbers * 100) / len(words)

print("Poziom naukowości testu =",result,"%")
