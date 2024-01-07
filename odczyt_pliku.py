file = input("Podaj nazwę pliku z danymi: ")

stream = open(file)
content = stream.read()
stream.close()

for digit in "0123456789":
    content = content.replace(digit,"X")

print("Zanonimizowany tekst to:")
print()
print(content)