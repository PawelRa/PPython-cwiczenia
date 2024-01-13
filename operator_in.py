# W ilu komentarzach pojawia się słowo
FILE_TO_READ = r"D:\Kodowanie na githubie\PPython-cwiczenia\pliki\comments.txt"
PUNCTATIONS = ".,?!:;"

with open(FILE_TO_READ) as stram:
    content = stram.read()

for punc in PUNCTATIONS:
    content = content.replace(punc,"")  
content = content.split(sep='\n')

text = input("Podaj słowa do sprawdzenia: ").lower()
words_to_check = text.split()
counter = 0
for line in content:
    line = line.lower()
    words = line.split()
    temp_counter = False
    for word in words:
        for check in words_to_check:
            if word == check:
                temp_counter = True
                break
    if temp_counter:
        counter += 1
        temp_counter = False

print('Liczba komentarzy zawierających', text, 'wynosi', counter)
