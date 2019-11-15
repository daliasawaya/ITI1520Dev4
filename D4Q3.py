#Cours ITI1520
#Auteur : Dalia Sawaya -- Hened Saade
#Numéro d’étudiant : 300111681 -- 300111592
print("Auteur: Hened Saade.  Numéro d’étudiant: 300111592 ")
print("Auteur: Dalia Sawaya. Numéro d’étudiant: 300111681")

###########################################################################
#########################   Devoir4-Question3    ##########################
###########################################################################

from jeuSudoku import *

def afficherGrille(grille):
    '''
    (list) -> None
    Affiche le grille de jeu Sudoku
    
    Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    print("   ", end="")
    col = 0
    while col < len(grille):
      print(col, end="  ")
      col += 1
    print()
    row = 0
    while row < len(grille):
       print(row, end="")
       col = 0
       while col < len(grille[row]):
         print(" ", grille[row][col], end="")
         col += 1
       print()
       row += 1

def jouer(grille, row, col, num):
    '''
    (list, int, int, int) -> Bool
    Jouer une étape de jeu Sudoku
    Preconditions: grille est une réference sur une liste de 9x9 contient seulement des nombres
    grille est modifié (un element est ajouté dans la grille) si la case est valide est correcte.
    '''

    #si fonction verifier valide retourne True, change le 0 par le num de l'usager
    if verifierValide(grille, row, col, num) == True :
        grille[row][col] = num
        return True #retourne True si verifier valide retourne True
    else:
        return False #retourne False si verifier valide ne retourne pas True
    

#PROGRAMME PRINCIPALE
    
# Créer le tableau de jeu (9 x 9)
grille = [[5, 3, 8, 6, 9, 1, 0, 4, 7],
          [7, 4, 6, 0, 3, 2, 8, 1, 9],
          [1, 9, 2, 0, 8, 4, 3, 5, 6],
          [8, 7, 1, 2, 6, 3, 4, 9, 5],
          [3, 2, 9, 4, 5, 7, 1, 6, 8],
          [4, 6, 5, 9, 1, 8, 7, 2, 3],
          [0, 0, 4, 3, 7, 9, 5, 8, 2],
          [9, 8, 3, 1, 0, 5, 6, 7, 4],
          [2, 5, 0, 8, 4, 6, 9, 3, 1]]  # la seule matrice utilisé dans le programme.
print("Menu: 1- Commencer un nouveau jeu.")
print("     ", "2- Continuer le jeu.")
print("     ", "3- Quitter le jeu.")

while True :
    try :
        choix = int(input("SVP entrez votre choix: 1, 2 ou 3: "))
        assert choix > 0 and choix < 4
        break
    except ValueError :
        print("Pas un entier, essayez encore une fois")
    except AssertionError :
        print("Entre entier entre 1 et 3 seulement")
    

while choix < 3 and choix > 0:
      if choix == 1:
          # Créer le tableau de jeu (9 x 9)
          grille = [[5, 3, 8, 6, 9, 1, 0, 4, 7],
                    [7, 4, 6, 5, 3, 2, 8, 1, 9],
                    [1, 9, 2, 7, 8, 4, 3, 5, 6],
                    [8, 7, 1, 2, 6, 3, 4, 9, 5],
                    [3, 2, 9, 4, 5, 7, 1, 6, 8],
                    [4, 6, 5, 9, 1, 8, 7, 2, 3],
                    [6, 1, 4, 3, 7, 9, 5, 8, 2],
                    [9, 8, 3, 1, 2, 5, 6, 7, 4],
                    [2, 5, 0, 8, 4, 6, 9, 3, 1]]  # la seule matrice utilisé dans le programme.
      afficherGrille(grille)

      while True :
        try :
            row = int(input("entrez votre choix de case ligne "))
            assert row > -1 and row < 9
            break
        except ValueError :
            print("Pas un entier, essayez encore une fois")
        except AssertionError :
            print("Entre entier entre 0 et 8 seulement")

      while True :
        try :
            col = int(input("entrez votre choix de case col "))
            assert col > -1 and col < 9
            break
        except ValueError :
            print("Pas un entier, essayez encore une fois")
        except AssertionError :
            print("Entre entier entre 0 et 8 seulement")

      while True :
        try :
            num = int(input("entrez votre choix de case num "))
            assert num > 0 and num < 10
            break
        except ValueError :
            print("Pas un entier, essayez encore une fois")
        except AssertionError :
            print("Entre entier entre 1 et 9 seulement")

      
      if grille[row][col] == 0:
          ajout = jouer(grille, row, col, num)
          
          if ajout == True:
              print("Bravo!!")
          else:
              print("Echec :(")
              
      else:
          print("Case deja rempli")
          
      afficherGrille(grille)
      
      if verifierGagner(grille) == True:
          print("Bravo!! Vous avez gagne")
          choix = -1
      else:
         print("Menu: 1- Commencer un nouveau jeu.")
         print("     ", "2- Continuer le jeu.")
         print("     ", "3- Quitter le jeu.")
         while True :
            try :
                choix = int(input("SVP entrez votre choix: 1, 2 ou 3: "))
                assert choix > 0 and choix < 4
                break
            except ValueError :
                print("Pas un entier, essayez encore une fois")
            except AssertionError :
                print("Entre entier entre 1 et 3 seulement")
if choix==3:
    print("Au revoir")
