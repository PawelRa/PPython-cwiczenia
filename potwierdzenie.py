import glob

pattern = input("Podaj ścieżkę: ")
pattern += r"\*.txt"
filenames = glob.glob(pattern)

print("Zostanie wyświetlona linia z poniższych plików tekstowych:")
for filename in filenames:
    print(filename)

choice = input("Aby kontynuować wciśnij klawisz T ")
if choice.lower() == "t":
    for filename in filenames:
        with open(filename, 'r') as stream:
            content = stream.read()
        lines = content.split('\n')
        first_line = lines[0]
        print(filename, '--->', first_line)
    print("KONIEC")
else:
    print("Anulowano wyświetlanie :( ")
