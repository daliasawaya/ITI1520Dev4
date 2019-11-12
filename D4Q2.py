#################################################
#################ITI 1520########################
#################################################

#Auteur: Hened Saade
#Numéro d'étudiant: 300111592

print("Auteur: Hened Saade")
print("Numéro d'étudiant: 300111592")

def modifierMat(matrice):
    ''' list -> list
    Prend une matrice (liste de listes) et retourne une nouvelle matrice.
    Tout les nombres paires de la matrice sont remplacés par leur racine carrée.
    '''
    i=0 #initialise i
    while i <len(matrice): #continue la boucle si i < que le nombre de colonnes
        j=0 #initialise j
        while j<len(matrice[0]): #continue la boucle si i < que le nombres de lignes
            if matrice[i][j]%2==0: #vérifie si le nombre est paire ou impaire
                matrice[i][j]= matrice[i][j]**(1/2) #si oui, sa change cette valeur à la racine carrée de cette element
            j=j+1 #incrémente j
        i=i+1 #incrémente i
    return matrice #retourne la nouvelle matrice avec les éléments changés
