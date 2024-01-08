file_path = "d:\Kodowanie na githubie\PPython-cwiczenia\pliki\expenses_ex.txt"

with open(file_path) as stream:
    content = stream.read()

expenses_list = content.split(sep='\n')

result = 0
for linia in expenses_list:
    if linia:
        expense = linia.split(maxsplit=1)
        result += float(expense[0])

print("Wydatki wynoszą -", result)
