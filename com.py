from random import randint
import heapq

class Computer(object):


    def __init__(self):
        self.allguess = [[[0, 0, 1, 1, 2], 2, 1]]
        pass

    def main(self):
        maxgen = 100
        maxsize = 60
        i = 1
        perf = 0
        bon = 0
        firstguess = [0, 0, 1, 2, 3]

        guess = None
        #Play first guess
        #Get response
        b, w = None
        self.allguess.append([firstguess, b, w])

        while perf != 5:
            i += 1
            h = 0
            CodeElligible = []
            #Create the first population
            pop = self.initPopulation()
            #Calculate the fitness of all the code in the generation
            fitpop = self.fitness(firstguess , *pop)
            #Get the indice of the 10 best of the generations
            indice = self.elitegeneration(fitpop)
            #Create a list with the 10 best code of this generation
            toppop = [pop[i] for i in indice]

            #loop for a maximaum au maxgen = 100 or with a maxsize of code chose of 60
            while( h <= maxgen and len(CodeElligible) <= maxsize):
                #Initialise a new generation of the populations
                #with the top 10 of the past generation
                pop = self.newPopulation(topop)

                fitpop = self.fitness(firstguess, pop)

                indice = self.elitegeneration(fitpop)

                #The top ten of my list to buil the next generations
                topop = [pop[i] for i in indice]

                CodeElligible.append(topop[0])

                h += 1

        #Play gues
        #Get reponse

    def initPopulation(self):
        #Cree une premiere population de 150 code randoms
        pop = []
        for i in range(150):
            z = True
            b = self.answer()
            for a in pop:
                if b == a:
                    z = False
                    break

            if z == True:
                pop.append(b)
        return pop

    def elitegeneration(self, a):
        #list of indice of the 10 best results of the fitness value
        return heapq.nlargest(10, range(len(a)), a.__getitem__)

    def answer(self):
        return [randint(0,7) for x in range(5)]

    def newPopulation(self, a):
        #Receive the top ten of the past generation
        #Take two randoms parents from the group and perform a cross-over
        #and all other operation (mutation, ...) with a small chance
        newpop = [] 
        p1, p2 = None, None
        while p1 != p2:
            p1, p2 = a[randint(0, len(a))], a[randint(0, len(a))]

        for i in range(150):
            child = self.crossover(p1, p2)
            if randint(0, 100) <= 10:
                child = self.mutation(child)
            if randint(0, 100) <= 10:
                child = self.permutation(child)
            if randint(0, 100) <= 10:
                child = self.inversion(child)

            while not newpop.__contains__(child):
                child = self.answer

    def crossover(self, a, b):
        #50/50 chance que se soit 1 ou 2 point crossover
        chance = randint(1,2)
        if chance == 1:
            #One point crossover
            point = randint(0,7)
            z, k = a[:point], b[point:]
            p = []
        elif chance == 2:
            #Two point crossover
            p1 = randint(0, 7)
            p2 = randint(0, 7)
            if p1 > p2:
                p2, p1 = p1, p2
            z, p, k = a[:p1], b[p1:p2], a[p2:] 
        return z + p + k

    def fitness(self, f, a):
        lis = []
        for i in a:
            b, w = self.verif(i[:], f[:])
            t, m = (sum([abs(b - q[1]) for q in self.allguess])), sum([abs(w - o[2]) for o in self.allguess])
            fit = 1 * t + m
            lis.append(fit)
        return lis

    def mutation(self, a):
        #Recoit un code une mets une couleur aleatoire a une couleur aleatoire
        a[randint(0,7)] = randint(0,7)
        return a
    
    def permutation(self, a):
        i1, i2 = self.yolo()
        a[i1], a[i2] = a[i2], a[i1]
        return a

    def inversion(self, a):
        i1, i2 = self.yolo()
        return self.reverse_sublist(a,i1,i2)

    def reverse_sublist(self, zoro, start, end):
        zoro[start:end] = zoro[start:end][::-1]
        return zoro

    def verif(self, a,  f):
        b = 0
        w = 0
        t = f
        for i, k in enumerate(f):
            if k == a[i]:
                b += 1
                t[i] = "!"
                a[i] = "?"
        for q in a:
            for i, h in enumerate(t[:]):
                if q == h:
                    w += 1
                    t[i] = "!"
                    break
        return b, w

    def yolo(self):
        i1 = randint(0,7)
        i2 = None
        while i2 != i1:
            i2 = randint(0,7)
        return i1, i2
