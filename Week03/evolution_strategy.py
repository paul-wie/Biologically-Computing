import random as rand

#parent selection, uniform random
#return: two randomly selected parents
def parent_selection(population):
    length = len(population)
    random1 = rand.randint(1,length-1)
    random2 = rand.randint(1,length-1)
    return population[random1], population[random2]




def main():
    population = [1,2,3,4]
    print(parent_selection(population))

main()
