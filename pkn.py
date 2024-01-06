print("Gra w papier, kamień, nożyce")
print("Dla zagrania papier wcisnij P, dla kamienia, K, dla nożyc n")

g1 = input("Zagranine pierwszego gracza: ")
g2 = input("Zagranine drugiego gracza: ")

if g1.lower() == "p" and g2.lower() == "p":
    print("Remis")
elif g1.lower() == "p" and g2.lower() == "k":
    print("Wygrywa gracz pierwszy")
elif g1.lower() == "p" and g2.lower() == "n":
    print("Wygrywa gracz drugi")
elif g1.lower() == "k" and g2.lower() == "k":
    print("Remis")
elif g1.lower() == "k" and g2.lower() == "n":
    print("Wygrywa gracz pierwszy")
elif g1.lower() == "k" and g2.lower() == "p":
    print("Wygrywa gracz drugi")
elif g1.lower() == "n" and g2.lower() == "n":
    print("Remis")
elif g1.lower() == "n" and g2.lower() == "p":
    print("Wygrywa gracz pierwszy")
elif g1.lower() == "n" and g2.lower() == "k":
    print("Wygrywa gracz drugi")
else:
    print("Wybrano złe zagrania. Powtórz rozgrywkę")