file = input("Podaj nazwę pliku z danymi: ")

with open(file) as stream:
    content = stream.read()


for digit in "0123456789":
    content = content.replace(digit,"X")

print("Zanonimizowany tekst to:")
print()
print(content)