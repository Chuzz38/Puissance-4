joueur1 = input("Ecrivez le nom du joueur 1 : ")
joueur2 = input("Ecrivez le nom du joueur 2 : ")
print(" ")


COLONNE = 7
LIGNE = 6


tableau = [['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.']]

def afficheTableau():
    for l in range (LIGNE):
        for c in range (COLONNE):
            print(tableau[l][c], end = " ")
        print()

def verifieLignes():
    pass


def ajoutePion(colonne, pion):
    for i in range (LIGNE-1, -1, -1):
        if tableau[i][colonne]==".":
            tableau[i][colonne] = pion
            print("placee en ligne",i)
            break


for i in range (21):
    afficheTableau()
    print(" ")
    print(joueur1,"c'est ton tour")
    print(" ")
    co = int(input("entrer une colonne "))
    ajoutePion(co, '@')

    afficheTableau()
    print(" ")
    print(joueur2,"c'est ton tour")
    print(" ")
    co = int(input("entrer une colonne "))
    ajoutePion(co, 'X')