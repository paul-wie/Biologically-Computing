import random as rand

def f1(x):
    return x

def f2(x):
    return x**2

#parent selection, lambiform random
#return: two randomly selected parents
def parent_selection(population):
    length = len(population)
    random1 = rand.randint(1,length-1)
    random2 = rand.randint(1,length-1)
    return population[random1], population[random2]

#survivor creation
#return 'number_of_survivor' survivor
def create_offspring(population, lamb):
    offspring = []
    while lamb > 0:
        parents = parent_selection(population)
        offspring.append( (parents[0]+parents[1]) /2 )
        lamb -=1
    return offspring

#select 'number_of_survivor' individuals for the next generation
def elitism(population, number_of_survivor):
    survivor = []
    if number_of_survivor > len(population) or number_of_survivor < 0:
        return population

    while number_of_survivor > 0:
        maximum = max(population)
        population.remove(maximum)
        survivor.append(maximum)
        number_of_survivor -=1
    return survivor

#simulates one generation
def generation(population,lamb):
    offspring = create_offspring(population,lamb)
    return elitism( population+offspring, len(population) )

#simulates several generations
def evolution(population,lamb,generations):
    while generations > 0:
        population = generation(population, lamb)
        generations -=1

    return population

def write_file(file, description, data):
    file.write(description)
    file.write(str(data))
    file.write("\n")

def main():
    population = [0,1,2,3,4]
    lamb = 10
    filename = "result.txt"
    file = open(filename, "w")

    write_file(file, "Start population:", population)
    write_file(file, "Population after " +str(lamb) + " generations:" , evolution(population, lamb, 3))

    file.close()

main()
