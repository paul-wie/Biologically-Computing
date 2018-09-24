import random as rand

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

#write result to a text file
def write_file(file, description, data):
    file.write(description)
    file.write(str(data))
    file.write("\n")

#increase lambda on the same population
def increase_lambda(population,lamb,generations,max_lambda,filename):
    file = open(filename, "w")
    while lamb <= max_lambda:
        write_file(file, "Generations:", generations)
        write_file(file, "Lambda:", lamb)
        write_file(file, "Start population:", population)
        write_file(file, "Final population" , evolution(population, lamb, generations))
        write_file(file, "------------------------------------------", "\n")
        lamb+=1
    file.close()
    #123

def increase_population(population, lamb, generations, max_generations,filename):
    file = open(filename, "w")
    while generations <= max_generations:
        write_file(file, "Generations:", generations)
        write_file(file, "Lambda:", lamb)
        write_file(file, "Start population:", population)
        write_file(file, "Final population" , evolution(population, lamb, generations))
        write_file(file, "------------------------------------------", "\n")
        generations+=1
    file.close()


def main():
    population = [0,1,2,3,4]
    lamb = 3
    #increase_lambda(population,lamb,3,20,"increase_lambda.txt")
    increase_population(population,lamb,1,30,"increase_population.txt")


main()
