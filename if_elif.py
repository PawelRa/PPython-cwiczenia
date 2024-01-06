mark = input("Podaj znak do sprawdzenia: ")
if len(mark) != 1:
    print("Należy podać 1 znak")
elif mark.isalpha():
    print("Podany znak jest literą")
elif mark.isdigit():
    print("Podany znak jest cyfrą")
elif mark.isspace():
    print("Podano biały znak")
else:
    print("Podano znak specjalny")