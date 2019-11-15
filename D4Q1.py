#Cours ITI1520
#Auteur : Dalia Sawaya -- Hened Saade
#Numéro d’étudiant : 300111681 -- 300111592
print("Auteur: Dalia Sawaya. Numéro d’étudiant: 300111681")
print("Auteur: Hened Saade.  Numéro d’étudiant: 300111592 ")

###########################################################################
#########################   Devoir4-Question1    ##########################
###########################################################################


def calculPrix(article, quantite) :
    #prend un article et la quantite demandee, et retourne le prix 
    
    '''
    (str, int) -> float
    '''
    
    global q
    global p

    #cherche le prix de l'article dans le dict p et multiplie par la quantite
    prix = p[article]*quantite

    return prix


def calculTotal(article1, quantite1, article2, quantite2, article3, quantite3) :
    #prend les 3 atricles et leur quantite, appelle la fonction calculPrix
    #retourne le prix totale
    
    '''
    (str, int, str, int, str, int) -> float
    '''

    #appele calculPrix pour calculer prix de chaque article et sa quantite
    prix1 = calculPrix(article1, quantite1)
    prix2 = calculPrix(article2, quantite2)
    prix3 = calculPrix(article3, quantite3)

    #ajoute tous les prix retournes ensemble
    prixTot = prix1 + prix2 + prix3

    return prixTot


def validerCommande(article1, quantite1, article2, quantite2, article3, quantite3) :
    '''
    (str, int, str, int, str, int) -> bool
    '''

    #prend les 3 atricles et leur quantite
    #verifie si il y a assez d'articles dans dict q que quantite pour cet article
    #retourne bool True pour oui et False pour non
    
    global q

    #verifire si les articles existent dans dict q
    if article1 not in q :
        return False
    elif article2 not in q :
        return False
    elif article3 not in q :
        return False

    #verifie si il y a assez de l'article dans dict q que veut l'usager
    elif quantite1>q[article1] :
        return False
    elif quantite2>q[article2] :
        return False
    elif quantite3>q[article3] :
        return False

    #si aucune des conditions ci-haut est bonne, retourne True: commande est valide
    else :
        return True

#PROGRAMME PRINCIPALE

#cree les 2 dictionnaires
q = {"bureau":9, "chaise":25, "imprimante":46, "scanneur":17}
p = {"bureau":75.9, "chaise":50.9, "imprimante":32.5, "scanneur":28.0}

#demande a l'usager pour entrer les articles et leur quantite
    
a1 = input("Entrer 1er article: ")

while True:
    try :
        q1 = int(input("Entrer quantite de 1er article: "))
        break
    except ValueError :
        print("Pas un entier, essayez encore une fois")
    
a2 = input("Entrer 2eme article: ")

while True:
    try :
        q2 = int(input("Entrer quantite de 2eme article: "))
        break
    except ValueError :
        print("Pas un entier, essayez encore une fois")
        
a3 = input("Entrer 3eme article: ")

while True:
    try :
        q3 = int(input("Entrer quantite de 3eme article: "))
        break
    except ValueError :
        print("Pas un entier, essayez encore une fois")
    

#si la commande n'est pas valide
if validerCommande(a1,q1,a2,q2,a3,q3) == False :
   print("Votre commande est annulée. SVP, vérifier les articles ou les quantités.")
   print("Les quantités et les articles disponibles sont:",q)

#si la commande est valide
   
else :
    print("Le prix total de votre commande est", calculTotal(a1,q1,a2,q2,a3,q3), "$")
    print("Merci et à la prochaine.")

    q[a1]=q[a1]-q1
    q[a2]=q[a2]-q2
    q[a3]=q[a3]-q3

    print("Les quantités et les articles disponibles sont:",q)

    
    
    
    
    

   
   
    
    





