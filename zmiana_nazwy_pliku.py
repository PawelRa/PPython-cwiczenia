NEW_EXTENSION = ".bak"
file_name = input("Podaj nazwę pliku: ")

if '.' in file_name:
    file_parts = file_name.rsplit('.', maxsplit=1)
    print(file_parts[0] + NEW_EXTENSION)
else:
    print(file_name)
