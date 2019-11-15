def verifierLigne(grille, row, num):
    '''
        (list, int, int) -> Bool
        Vérifier si la case à ajouter n'existe pas sur la ligne.
        Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''

    for i in range (9) :
        if grille[row][i] == num :
            print("Row False")
            return False
    return True
    

def verifierCol(grille, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la colonne.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    for j in range (9) :
        if grille[j][col]==num:
            print("Col False")
            return False
    return True

def verifierSousGrille(grille, row, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la sous-grille.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''

    #BIG ROW 1

    if 0<=row<=2 and 0<=col<=2 :
        for i in range (3) :
            for j in range (3) :
                if grille[i][j] == num :
                    print("False 1")
                    return False

    if 0<=row<=2 and 3<=col<=5 :
        for m in range (3) :
            for n in range (3,6) :
                if grille[m][n] == num :
                    print("False 2")
                    return False

    if 0<=row<=2 and 6<=col<=8 :
        for q in range (3) :
            for p in range (6,9) :
                if grille[q][p] == num :
                    print("False 3")
                    return False
    #BIG ROW 2
    
    if 3<=row<=5 and 0<=col<=2 :
        for k in range (3,6) :
            for h in range (3) :
                if grille[k][h] == num :
                    print("False 4")
                    return False

    if 3<=row<=5 and 3<=col<=5 :
        for k in range (3,6) :
            for h in range (3,6) :
                if grille[k][h] == num :
                    print("False 5")
                    return False

    if 3<=row<=5 and 6<=col<=8 :
        for k in range (3,6) :
            for h in range (6,9) :
                if grille[k][h] == num :
                    print("False 6")
                    return False
    #BIG ROW 3
    
    if 6<=row<=8 and 0<=col<=2 :
        for l in range (6,9) :
            for s in range (3) :
                if grille[l][s] == num :
                    print("False 7")
                    return False
            
    if 6<=row<=8 and 3<=col<=5 :
        for a in range (6,9) :
            for b in range (3,6) :
                if grille[a][b] == num :
                    print("False 8")
                    return False

    if 6<=row<=8 and 6<=col<=8 :
        for y in range (6,9) :
            for z in range (6,9) :
                if grille[y][z] == num :
                    print("False 9")
                    return False
    
    return True

    

def verifierGagner(grille):
    '''(list) ->  bool
    * Preconditions: grille est une reference a une matrice 9x9 qui contient de nombres de 1 à 9
    * Verifie si la grille est completement remplie.
    '''
    
   # A COMPLETER
  
def verifierValide(grille, row, col, num):
   ''' (list, int, int, int) ->  bool
   * verifie si le nombre proposé est bon sur la ligne et colonne et la sous-grille donné en parametre.
   * Preconditions: tab est une reference a une matrice 9 x 9 qui contient des chiffres entre 1 et 9
   '''
   
   # A COMPLETER
   

