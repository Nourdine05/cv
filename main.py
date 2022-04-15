import random



NB_MIN = 1
NB_MAX = 100
NB_Q = 10


def poser_question(NB_MIN,NB_MAX):
    a = random.randint(NB_MIN,NB_MAX)
    b = random.randint(NB_MIN,NB_MAX)
    o = random.randint(0,1)
    operateur_str = "+"
    if o == 1:
        operateur_str = "*"
   
    reponse_str = input(f" Calculez : {a} {operateur_str} {b} = ")
    reponse_int = int(reponse_str)
    calcul = a+b
    if reponse_int == a+b :
       
        return True
    

    return False
        # print("Réponse incorrect")
NB_PTS = 0        
for i in range (0,NB_Q):
    print(f"Question n: {i+1} sur {NB_Q}: ")
    if  poser_question(NB_MIN,NB_MAX):
         # print("Réponse correcte")
       NB_PTS += 1
    else :
        # print("Réponse incorrect")
         print()
         
print(f"Votre notes est {NB_PTS}/{NB_Q}")

moyenne = int(NB_Q/2)

if NB_PTS >= 8:
    print("Exellent")
elif NB_PTS > moyenne:
    print("Peux mieux faire")
elif NB_PTS == 0:
    print(" revise !")
elif NB_PTS < moyenne:
    print("Manque d'efforts")
    
    
input()



