import glob

NEW_EXTENSION = ".bak"
file_path = input("Podaj ścieżkę: ")
file_path += r"\*.txt"

files = glob.glob(file_path)
for file in files:
    if '.' in file:
        file_parts = file.rsplit('.', maxsplit=1)
        file_path_parts = file_parts[0].rsplit("\\", maxsplit=1)
        print("zamiana ", file, "na", file_path_parts[1] + NEW_EXTENSION)
    else:
        print(file)
