import glob
import os

NEW_EXTENSION = ".bak"
file_path = input("Podaj ścieżkę: ")
file_path += r"\*.txt"

files = glob.glob(file_path)

file_names = []
for file in files:
    if '.' in file:
        file_name, extension = file.rsplit('.', maxsplit=1)
        file_names.append([file, file_name + NEW_EXTENSION])
    else:
        print(file)

print("Czy chcesz zmienić poniższe pliki?")
for file in file_names:
    print(file[0], "--->", file[1])

test = input("T/N ")

if (test.lower() == 't'):
    for old, new in file_names:
        os.rename(old, new)
    print("Nazwy zostały zmienione")
else:
    print("Anulowano zmiany")
