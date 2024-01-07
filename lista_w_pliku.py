file_path = "pliki\expenses.txt"
with open(file_path) as stream:
    raw_expenses = stream.read()

expenses_in_table = raw_expenses.split()
expenses = 0
for expens in expenses_in_table:
    expenses += float(expens)

print("Wydatki wynoszą", expenses)
