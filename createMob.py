from genMob import *

def createMob():
   list_nommob = ["Maiga", "Naro", "Bad"]
   monstre = random.choice(list_nommob)
   return genMob(monstre)
