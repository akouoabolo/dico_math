import random
import num2words
nombre=23
nombre_en_lettres = num2words.num2words(nombre, lang='fr')
print( nombre_en_lettres)
def convertir_en_lettres(nombre):
    nombre_en_lettres = num2words.num2words(nombre, lang='fr')
    return nombre_en_lettres

print("Bonjour! Cette application est destinée aux élèves de CE1.")
reponse = input("Êtes-vous prêt à commencer l'exercice? (oui/non) ")

if reponse.lower() == "oui":
    nombres = []
    for i in range(5):
        nombres.append(random.randint(1, 100))
    print("Voici 5 nombres aléatoires : ", nombres)

    ordre = input("Souhaitez-vous classer les nombres par ordre croissant ou décroissant? (croissant/décroissant) ")

    if ordre.lower() == "croissant":
        nombres_tries = sorted(nombres)
    elif ordre.lower() == "décroissant":
        nombres_tries = sorted(nombres, reverse=True)
    else:
        print("Je n'ai pas compris votre réponse. Aurevoir!")
        exit()

    print("Veuillez ranger les nombres suivants dans l'ordre que vous avez choisi : ", nombres_tries)
    reponse_utilisateur = input("Entrez les nombres séparés par des virgules : ")
    reponse_utilisateur_liste = list(map(int, reponse_utilisateur.split(",")))

    while reponse_utilisateur_liste != nombres_tries:
        print("Dommage! Vous n'avez pas correctement classé les nombres. Recommencez s'il vous plaît.")
        reponse_utilisateur = input("Entrez les nombres séparés par des virgules : ")
        reponse_utilisateur_liste = list(map(int, reponse_utilisateur.split(",")))

    print("Bravo! Vous avez correctement classé les nombres.")
    print("Maintenant, voici les nombres dans un ordre aléatoire, écrivez-les en lettres : ")
    random.shuffle(nombres)
    nombres_en_lettres = []
    for nombre in nombres:
        nombre_en_lettres = convertir_en_lettres(nombre)
        nombres_en_lettres.append(nombre_en_lettres)
    print("Les nombres en chiffres sont : ",  reponse_utilisateur_liste)
    reponse_utilisateur_lettres = input("Entrez les nombres en lettres séparés par des virgules : ")
    reponse_utilisateur_lettres_liste = reponse_utilisateur_lettres.split(",")

    #while reponse_utilisateur_lettres_liste != nombres_en_lettres:
       #print("Dommage! Vous n'avez pas correctement classé les nombres en lettres. Recommencez s'il vous plaît.")
        #reponse_utilisateur_lettres = input("Entrez les nombres en lettres séparés par des virgules : ")
        #reponse_utilisateur_lettres_liste = reponse_utilisateur_lettres.split(",")
        
    while not all(nombre in nombres_en_lettres for nombre in reponse_utilisateur_lettres_liste):
            print("Dommage! Vous n'avez pas correctement classé les nombres en lettres. Recommencez s'il vous plaît.")
            reponse_utilisateur_lettres = input("Entrez les nombres en lettres séparés par des virgules : ")
            reponse_utilisateur_lettres_liste = reponse_utilisateur_lettres.split(",")

    print("Bravo! Vous avez correctement classé les nombres en lettres.")
    print("Bravo! Vous avez terminé l'exercice.")
else:
    print("Aurevoir et à bientôt!")