from random import randint

class Computer(object):


    def __init__(self):
        pass


    def main(self):
    	maxgen = 100
    	maxsize = 60
        i = 1
        perf = 0
        bon = 0
        firstguess = [0,0,1,1,2]
        guess = None

        #Play first guess
        #Get response

        # ?? p
        while perf != 5:
        	i += 1
        	h = 0
        	CodeElligible = []
        	pop = self.initPopulation()

        	while( h <= maxgen and len(CodeElligible) <= maxsize):
        		pop = self.newPopulation(pop)

        		if self.fitness():
        			CodeElligible.append(guess)

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
    		if z = True:
    			pop.append(b)		
    	return pop


    def answer(self):
    	return [randint(0,7) for x in range(5)]

    def newPopulation(self):
    	pass

    def crossover(self, a):
    	pass


    def fitness(self, a, f):
    	b, w = verif(a, f)

    	fitness = 2(b + w) + sum(range(1, b+w))
    	return fitness

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
    	return reverse_sublist(a,i1,i2)

    def reverse_sublist(zoro,start,end):
    	zoro[start:end] = zoro[start:end][::-1]
    	return zoro

    def verif(a, f):
    	b = 0
    	w = 0
    	t = f
    	for i, k in enumerate(f):
			if k == a[i]:
		 	    b += 1
				t[i] = "!"
				a[i] = "?"
		for q in a:
			for i, h in enumerate([:]):
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


        
