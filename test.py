
from com import Computer


a = Computer()

firstguess = [0, 0, 1, 2, 3]
pop = a.initPopulation()

fitness = a.fitness(firstguess, pop)
print(fitness)