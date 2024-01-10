import glob
import os

NEW_EXTENSION = ".bak"
file_path = input("Podaj ścieżkę: ")
file_path += r"\*.txt"

files = glob.glob(file_path)
for file in files:
    if '.' in file:
        file_parts = file.rsplit('.', maxsplit=1)
        os.rename(file, file_parts[0] + NEW_EXTENSION)
        print("Nowy plik =", file_parts[0] + NEW_EXTENSION)
    else:
        print(file)
