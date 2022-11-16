import random
 
jouer = "o"
while jouer == "o" :
    print("Jeu du nombre secret")
    print("Le but du jeu étant de deviner un nombre comportant trois chiffres, le jeu vous indiquera si votre proposition est plus grand ou plus petit que le nombre secret. Bonne chance ! ")
    print("Vous pouvez quitter à tout moment en appuyant sur Q")
    r = random.randint(100,999)
    print(r)
    a = "0"
    i=0
 
    while( a != r ):
        i+=1
        a = input("Proposez un chiffre entre 100 et 999 : ")
        try :
            a = int(a)
            if a > 99 and a < 1000 :
                if a < r :
                    print("Le nombre est plus grand !")
                elif a > r :
                    print("Le nombre est plus petit !")
                else:
                    print("Bravo, vous avez gagné le nombre était bien",r,'!' )
                    print("Votre nombre d'essai(s) est",i)
            else :
                print("Votre choix n'est pas compris entre 100 et 999.")
        except :
            if a.lower() == "q" :
                break
            else :
                print("Vous n'avez ni entré un nombre ni appuyé sur la touche Q.")
 
    jouer = input("Voulez-vous recommencer ? o/n").lower()
 
print("Vous avez quitté le jeu")
