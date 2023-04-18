def string(type, saison):
    if type == "fruits" and saison =="hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "été":
        print("poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legume" and saison == "été":
        print("artichaut, aubergine, navet")

string("fruits", "hiver")
string("fruits", "été")
string("legume", "hiver")
string("legume", "été")