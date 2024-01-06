password = input("Podaj hasło do weryfikacji: ")

has_lower = 0
has_upper = 0
has_no_space = 1
has_special = 0
length = len(password) > 7

for char in password:
    if char.islower():
        has_lower = 1
    elif char.isupper():
        has_upper = 1
    elif char == " ":
        has_no_space = 0
    elif (not char.isspace()) and (not char.isalpha()) and (not char.isdigit()):
        has_special = 1

print()
if has_special + has_no_space + has_lower + has_upper + length == 5:
    print ("Hasło jest prawidłowe")
else:
    if len(password) < 8:
        print("Hasło musi zawierać minimum 8 znaków")
    if has_lower == 0:
        print("Hasło musi posiadać minimum jedną małą literę")
    if has_upper == 0:
        print("Hasło musi posiadać minimum jedną dużą literę")
    if has_no_space == 0:
        print("Hasło nie może posiadać spacji")
    if has_special == 0:
        print("Hasło musi posiadać minimum jeden znak specjalny")
