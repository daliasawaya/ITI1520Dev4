#Cours ITI1520
#Auteur : Dalia Sawaya -- Hened Saade
#Numéro d’étudiant : 300111681 -- 300111592

###########################################################################
####################   Devoir4-Question3-jeuSudoku    #####################
###########################################################################


def verifierLigne(grille, row, num):
    '''
        (list, int, int) -> Bool
        Vérifier si la case à ajouter n'existe pas sur la ligne.
        Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''

    #boucle qui verifie si num de l'usager est deja dans la ligne (row) que l'usager veut
    #i prend la valeur des colonnes qu'on veut verifier, i commence a 0 et fini a 8 
    for i in range (9) :
        # si on trouve num de l'usager dans la ligne, retourne False
        if grille[row][i] == num :
            return False
    #si on ne trouve pas le nunm dans la ligne, retourne True
    return True
    

def verifierCol(grille, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la colonne.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    #boucle qui verifie si num de l'usager est deja dans la colonne que l'usager veut
    #j prend la valeur des colonnes qu'on veut verifier, i commence a 0 et fini a 8
    for j in range (9) :
        # si on trouve num de l'usager dans la colonne, retourne False
        if grille[j][col]==num:
            return False
    #si on ne trouve pas le nunm dans la ligne, retourne True
    return True

def verifierSousGrille(grille, row, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la sous-grille.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''


    #3 CASES DU HAUT :



    #si c'est la 1ere case:
    if 0<=row<=2 and 0<=col<=2 :
        #boucle qui change valeur de i (rangees) de 0 a 2 (car 1ere case)
        for i in range (3) :
            #boucle dans boucle qui change valeur de j (colonnes) de 0 a 2 (car 1ere case)
            for j in range (3) :
                #si une des 9 valeurs dans case = au num de l'usager, retourne False
                if grille[i][j] == num :
                    return False

    #si c'est la 2e case:
    if 0<=row<=2 and 3<=col<=5 :
        #boucle qui change valeur de m (rangees) de 0 a 2 (car 2e case)
        for m in range (3) :
            #boucle dans boucle qui change valeur de n (colonnes) de 3 a 5 (car 1ere case)
            for n in range (3,6) :
                #si une des 9 valeurs dans case = au num de l'usager, retourne False
                if grille[m][n] == num :
                    return False

    #si c'est la 3e case:
    if 0<=row<=2 and 6<=col<=8 :
        #boucle qui change valeur de q (rangees) de 0 a 2 (car 3e case)
        for q in range (3) :
            #boucle dans boucle qui change valeur de p (colonnes) de 6 a 8 (car 3e case)
            for p in range (6,9) :
                #si une des 9 valeurs dans case = au num de l'usager, retourne False
                if grille[q][p] == num :
                    return False


                
    #3 CASES DU MILIEU : 



    #si c'est la 4e case:
    if 3<=row<=5 and 0<=col<=2 :
        #boucle qui change valeur de k (rangees) de 3 a 5 (car 4e case)
        for k in range (3,6) :
            #boucle dans boucle qui change valeur de h (colonnes) de 0 a 2 (car 4e case)
            for h in range (3) :
                #si une des 9 valeurs dans case = au num de l'usager, retourne False
                if grille[k][h] == num :
                    return False
                
    #si c'est la 5e case:
    if 3<=row<=5 and 3<=col<=5 :
        #boucle qui change valeur de k (rangees) de 3 a 5 (car 5e case)
        for k in range (3,6) :
            #boucle dans boucle qui change valeur de h (colonnes) de 3 a 5 (car 5e case)
            for h in range (3,6) :
                #si une des 9 valeurs dans case = au num de l'usager, retourne False
                if grille[k][h] == num :
                    return False
                
    #si c'est la 6e case:
    if 3<=row<=5 and 6<=col<=8 :
        #boucle qui change valeur de k (rangees) de 3 a 5 (car 6e case)
        for k in range (3,6) :
            #boucle dans boucle qui change valeur de h (colonnes) de 6 a 8 (car 6e case)
            for h in range (6,9) :
                #si une des 9 valeurs dans case = au num de l'usager, retourne False
                if grille[k][h] == num :
                    return False


                
    #3 CASES DU BAS :


                
    #si c'est la 7e case:
    if 6<=row<=8 and 0<=col<=2 :
        #boucle qui change valeur de l (rangees) de 6 a 8 (car 7e case)
        for l in range (6,9) :
            #boucle dans boucle qui change valeur de s (colonnes) de 0 a 2 (car 7e case)
            for s in range (3) :
                #si une des 9 valeurs dans case = au num de l'usager, retourne False
                if grille[l][s] == num :
                    return False
          
    #si c'est la 8e case:       
    if 6<=row<=8 and 3<=col<=5 :
        #boucle qui change valeur de a (rangees) de 6 a 8 (car 8e case)
        for a in range (6,9) :
            #boucle dans boucle qui change valeur de b (colonnes) de 3 a 5 (car 8e case)
            for b in range (3,6) :
                #si une des 9 valeurs dans case = au num de l'usager, retourne False
                if grille[a][b] == num :
                    return False
                
    #si c'est la 9e case:
    if 6<=row<=8 and 6<=col<=8 :
        #boucle qui change valeur de y (rangees) de 6 a 8 (car 9e case)
        for y in range (6,9) :
            #boucle dans boucle qui change valeur de z (colonnes) de 6 a 8 (car 9e case)
            for z in range (6,9) :
                #si une des 9 valeurs dans case = au num de l'usager, retourne False
                if grille[y][z] == num :
                    return False

                
                
    #si num on ne trouve pas num dans aucune des colonnes, rangees, ou cases:
    return True

    

def verifierGagner(grille):
    '''(list) ->  bool
    * Preconditions: grille est une reference a une matrice 9x9 qui contient de nombres de 1 à 9
    * Verifie si la grille est completement remplie.
    '''

    #boucles qui verifient si il reste des cases avec 0
    for d in range (9) :
        for e in range (9) :
            #si oui, retourne False car jeu n'est pas fini
            if grille[d][e] == 0 :
                return False
    #si non, retourne True, jeu est fini
    return True
    
  
def verifierValide(grille, row, col, num):
   ''' (list, int, int, int) ->  bool
   * verifie si le nombre proposé est bon sur la ligne et colonne et la sous-grille donné en parametre.
   * Preconditions: tab est une reference a une matrice 9 x 9 qui contient des chiffres entre 1 et 9
   '''

   #appelle fonction verifierLigne, si False, retourne False
   if verifierLigne(grille, row, num) == False :
        return False
    
   #appelle fonction verifierCol, si False, retourne False
   if verifierCol(grille, col, num) == False :
        return False

   #appelle fonction verifierSousGrille, si False, retourne False
   if verifierSousGrille(grille, row, col, num) == False:
        return False

   #retourne True si jamais retourne False 
   return True   

