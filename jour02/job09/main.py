def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("Le triangle est équilatéral")
        elif a == b or b == c or a == c:
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
                print("Le triangle est isocèle et rectangle")
            else:
                print("Le triangle est isocèle")
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Le triangle est rectangle")
        else:
            print("Le triangle est quelconque")
    else:
        print("Impossible de construire un triangle avec ces longueurs.")

triangle(3, 4, 5)
triangle(2, 2, 3)
triangle(1, 1, 1)
triangle(3, 0, 0)