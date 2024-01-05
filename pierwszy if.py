mark = input("Podaj znak do sprawdzenia: ")
if len(mark) != 1:
    print("Należy podać 1 znak")
elif (len(mark) == 1) and (mark.isalpha()):
    print("Podany znak jest literą")
elif (len(mark) == 1) and (mark.isalpha()==False):
    print("Podany znak jest czymś innymi niż litera")