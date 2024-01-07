file = input("Podaj nazwę pliku z danymi: ")
target = input("Podaj nazwę pliku do zapisu: ")
print("-------")

with open(file) as stream:
    content = stream.read()

for digit in "0123456789":
    content = content.replace(digit,"X")

if target: # sprawdzenie czy string ma zawartość - True ma, False jest pusty ("")
    with open(target, 'x') as writer:
        writer.write(content)
else:
    print("Nie wybrano pliku do zapisu")
    print(content)

print("Koniec programu")
