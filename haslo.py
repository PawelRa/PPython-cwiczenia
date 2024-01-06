password = input("Podaj hasło do sprawdzenia: ")

for char in password: 
    if char.isalpha():
        type_ = "jest literą"
    elif char.isdigit():
        type_ = "jest cyfrą"
    elif char.isspace():
        type_ = "jest białym znakiem"
    else:
        type_ = "jest znakiem specjalnym"

    print(char, type_)