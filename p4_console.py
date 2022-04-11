from p4_game import *

class P4_console:
    def __init__(self, nl = 6, nc = 7, jeton=('@','X')):
        self.nl = nl
        self.nc = nc
        self.jeton = jeton
        self.nbTours = 0
        self.p4 = P4_game()

    def jetonJoueur(self, jeton, joueur):
        pass

    def tourJoueur(self, joueur, nbTours):
        if nbTours % 2 == 0:
            return joueur[0] #1
        else:
            return joueur[1] #2
                
    def joueurs(self, joueur):
        joueur1 = input("Ecrivez le nom du joueur 1 : ")
        joueur2 = input("Ecrivez le nom du joueur 2 : ")
        pass # ?

    def coup_joueur(self, joueur):
        print(" ") #meme que ajoutePion ?

    def afficheTableau(self):
        for l in range (nl):
            for c in range (nc):
                print(self.P4_game.get_case([l][c]), end = " ")
            print()

    def ajoutePion(self, colonne, joueur):
        P4_game.placer_jeton(colonne, joueur)




"""Il faut définir joueur avant de commencer le jeu"""
print("Joueur n°1, donnez votre nom :")
joueur1 = input()
print("Joueur n°2, donnez votre nom :")
joueur2 = input()
#Mieux le définir et demander joueur1 et joueur2
nl = 0
nc = 0
nbTours = 0
#le changer à chaque fois que le joueur jou
joueur = joueur1
while not P4_game.verifier_victoire(nl, nc, joueur) or nbTours == 42:
    
    """a chaque fois que coup joué on mets nb Tours +1"""
    nbTours += 1
    
    P4_console.afficheTableau()
    print(" ")
    print(joueur,"c'est ton tour")
    print(" ")
    if not P4_game.placement_possible():
        print("Vous devez rejouer")
        colonne = int(input())
    else:
        P4_console.ajoutePion(colonne, joueur)  
    """while not ajoutePion # tant que le coup n'a pas été joué on reste sur le joueur.
    fonction qui renvoie true quand le coup a été joué, ou un truc du genre tu connais"""