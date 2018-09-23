import random as rand

#parent selection, uniform random
#return: two randomly selected parents
def parent_selection(population):
    length = len(population)
    random1 = rand.randint(1,length-1)
    random2 = rand.randint(1,length-1)
    return population[random1], population[random2]

#survivor creation
#select randomly two parents and create one new child
#return 'number_of_survivor' survivor
def survivor_creation(population, number_of_survivor):
    survivor = []
    while number_of_survivor > 0:
        parents = parent_selection(population)
        survivor.append( (parents[0]+parents[1]) /2 )
        number_of_survivor -=1
    return survivor


def main():
    population = [1,2,3,4]
    print(survivor_creation(population,8))

main()
