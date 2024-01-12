# W ilu komentarzach pojawia się słowo
FILE_TO_READ = r"D:\Kodowanie na githubie\PPython-cwiczenia\pliki\comments.txt"
PUNCTATIONS = ".,?!:;"

with open(FILE_TO_READ) as stram:
    content = stram.read()

for punc in PUNCTATIONS:
    content = content.replace(punc,"")  
content = content.split(sep='\n')

word = input("Podaj słowo do sprawdzenia: ").lower()
counter = 0
for line in content:
    line = line.lower()
    words = line.split()
    if word in words:
        counter += 1

print("Słowo ", word, "występuje", counter, "razy.")