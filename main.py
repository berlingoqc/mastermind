import sys
import os
from random import randint


class MasterMind(object):

    def __init__(self):
        self.couleur = ['rouge','bleu','vert','jaune','noire','kaki','aqua','orange']
        self.c = [i[0] for i in self.couleur]
        if len(sys.argv) > 1:
            if sys.argv[1] in ('1','2'):
                if self.start_player():
                    os.system('clear')
                    self.menu()
        else:
            print(self.menu())

    def menu(self):
        print("Bienvenue dans mon jeu de MasterMind\n\n1- Game ordinateur\n2- Game joueur\n3- Out of here")
        a = int(input("Ton choix :"))
        if a == 2:
            self.start_player()
    def create_awnser(self):
        return [self.couleur[randint(0,7)] for x in range(5)]
    def start_player(self):
        for i in self.couleur:
            print(i, end=" ")
        print("\n!!!!! Good luck !!!!!")
        self.answer = self.create_awnser()
        tAnswer = self.answer[:]
        find = ['_' for i in range(5)]
        nbrEssai = 0
        nbrCorrecte = 0
        nbrParfait = 0

        print(self.answer)

        while True:
            nbrCorrecte = 0
            nbrParfait = 0
            print(' '.join(find) + " essai # {}".format(nbrEssai))
            tAnswer = self.answer[:]
            essai = input()
            essai = list(essai)
            if self.valid_answer(essai):
                nbrEssai += 1
                for i, a in enumerate(self.answer):
                    if a[0] == essai[i]:
                        nbrParfait += 1
                        find[i] = a[0]
                        tAnswer[i] = "!"
                        essai[i] = "?"
                for a in essai:
                    for i, b in enumerate(tAnswer[:]):
                        if a == b[0]:
                            nbrCorrecte += 1
                            tAnswer[i] = "!"
                            break
                print("Correcte : {0} Parfait : {1}".format(nbrCorrecte,nbrParfait))
                if nbrParfait == 5:
                    print("Victoire en {}".format(nbrEssai))
                    input("Touche Enter pour continuer")
                    return True
                else:
                    print("Pas valid !")

    def valid_answer(self, a):
        if len(a) > 0:
            for i in list(a):
                if i not in self.c:
                    return False
            return True
        else:
            return False


if __name__ == "__main__":
    MasterMind()
