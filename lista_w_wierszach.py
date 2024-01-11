file_path = r"d:\Kodowanie na githubie\PPython-cwiczenia\pliki\expenses_ex.txt"

with open(file_path) as stream:
    content = stream.read()

expenses_list = content.split(sep='\n')

expenses = []
for linia in expenses_list:
    if linia:
        expense = linia.split(maxsplit=1)
        expenses.append(float(expense[0]))

suma = sum(expenses)
minimum = min(expenses)
maximum = max(expenses)
average_cost = suma / len(expenses)


print("Wszystkie wydatki wynoszą -", suma)
print("Najniższy wydatek =", minimum)
print("Najwyższy wydatek =", maximum)
print("Średni wydatek =", average_cost)
