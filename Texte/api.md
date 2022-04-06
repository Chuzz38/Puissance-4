Documentation de notre classe Puissance 4:

On initialise d'abord les attributs : -le nombre de lignes : nl qui est égale à 6 -le nombre de colonnes : nc qui est égale à 7 -le jeton selon le joueur : 1 pour le joueur 1 et 2 pour le joueur 2 -la tableJeu qui est défini par un rectangle de ligne * colonne composé de 0

Les différentes méthodes sont: -get_case(ligne, colonne) qui prend en parametres une ligne et une colonne et qui renvoie ce qui a dans la case correspondant à la ligne et la colonne, soit ça renvoie 0 : la case et vide, soit cela renvoie 1 et la case a déjà été joué par le jouer 1 et sinon ça renvoie 2 : la case a déjà été joué par le joueur 2.

-placement_possible(colonne) qui prend en parametre juste la colonne et qui renvoie True si
la colonne est jouable et False sinon

-placer_jeton(joueur, colonne) qui prend en paramètre le joueur qui joue et la colonne où le joueur veut
jouer. Il renvoie "Vous ne pouvez pas jouer dans cette colonne" si la colonne n'est pas disponible et 
sinon il modifie la tableJeu.

-verifier_victoire(ligne, colonne, joueur) qui prend en paramètre la ligne et la colonne où le jouer vient 
de jouer son pion. La méthode renvoie True si le coup qui vient d'être joué a permis la victoire et False sinon.
