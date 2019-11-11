#Cours ITI1520
#Auteur : Dalia Sawaya
#Numéro d’étudiant : 300111681
print("Auteur: Dalia Sawaya. Numéro d’étudiant: 300111681")
print("Auteur: Hened Saade.  Numéro d’étudiant: 300111592 ")

###########################################################################
#########################   Devoir4-Question1    ##########################
###########################################################################

#fonction nommee calculePrix, partie a)
#parametres: nom de l'article et la quantite
#calcule le prix de la quantite de l'article choisi
#retourne le prix 
def calculePrix(article,quantite) :
    '''
    (str, int) -> float
    '''
    if article == "bureau" :
        prix = 75.9 * quantite

    if article == "chaise" :
        prix = 50.9 * quantite

    if article == "imprimante" :
        prix = 32.5 * quantite

    if article == "scanneur" :
        prix = 28.0 * quantite

    return prix

#fonction nommee calculTotal, partie b)
#parametres: nom de 3 articles et leur quantite
#invoque fonction 'calculePrix' 3 fois
#calcule et retourne le prix totale
def calculTotal(article1, quantite1, article2, quantite2, article3, quantite3) :
    
    prix1 = calculePrix(article1,quantite1)
    prix2 = calculePrix(article2,quantite2)
    prix3 = calculePrix(article3,quantite3)
    
    prix_total = prix1 + prix2 + prix3

    return prix_total

def validerCommande(article1, quantite1, article2, quantite2, article3, quantite3) :

    #initialiser valide a True
    valide = True
    
    #verifie si un des articles est le bureau,
    #si oui: verifie si quantite est plus que 9
    #si oui: retourne false
    
    if (article1 == "bureau") :
        if quantite1>9 :
            valide = False
            
    if (article2 == "bureau") :
        if quantite2>9 :
            valide = False
        
    if (article3 == "bureau") :
        if quantite3>9 :
            valide = False

        
    #verifie si un des articles est le bureau,
    #si oui: verifie si quantite est plus que 25
    #si oui: retourne false
        
    if (article1 == "chaise") :
        if quantite1>25 :
            valide = False

    if (article2 == "chaise") :
        if quantite2>25 :
            valide = False
        
    if (article3 == "chaise") : 
        if quantite3>25 :
            valide = False

    #verifie si un des articles est le bureau,
    #si oui: verifie si quantite est plus que 46
    #si oui: retourne false

    if (article1 == "imprimante") :
        if quantite1>46 :
            valide = False

    if (article2 == "imprimante") :
        if quantite2>46 :
            valide = False
            
    if (article3 == "imprimante") :
        if quantite3>46 :
            valide = False

    #verifie si un des articles est le bureau,
    #si oui: verifie si quantite est plus que 17
    #si oui: retourne false
        
    if (article1 == "scanneur") :
        if quantite1>17 :
            valide = False

    if (article2 == "scanneur") :
        if quantite2>17 :
            valide = False
            
    if (article3 == "scanneur") :
        if quantite3>17 :
            valide = False


    #verifie si chaque article existe dans le magasin
    #si non: valide = false
    
    if (article1 != "bureau") and (article1 != "chaise") and (article1 != "imprimante") and (article1 != "scanneur") :
       valide = False

    if (article2 != "bureau") and (article2 != "chaise") and (article2 != "imprimante") and (article2 != "scanneur") :
       valide = False

    if (article3 != "bureau") and (article3 != "chaise") and (article3 != "imprimante") and (article3 != "scanneur") :
       valide = False

    return valide

#demande a l'usager d'entrer les donnees
A1 = input("Entrez le premier article: ")
Q1 = int(input("Entrez la quantité de votre 1ere article: "))
A2 = input("Entrez le deuxieme article: ")
Q2 = int(input("Entrez la quantité de votre 2eme article: "))
A3 = input("Entrez le troisieme article: ")
Q3 = int(input("Entrez la quantité de votre 3eme article: "))

#invoque methode validerCommande pour valider si les entrees de l'usager 
commande_valide = validerCommande(A1, Q1, A2, Q2, A3, Q3)


if commande_valide == True :
    prixTot = calculTotal(A1, Q1, A2, Q2, A3, Q3)
    str_prixTot = str(prixTot)
    print("Le prix total de votre commande est : "+str_prixTot+"$. Merci et à la prochaine.") 

if commande_valide == False :
    print("Votre commande est annulée. SVP, vérifier les articles ou les quantités.")
    
