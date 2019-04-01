from common import *
from timeit import default_timer as timer
import random as rand
import numpy as np
import matplotlib.pyplot as plt
#import pmx algorithm
from PMX import do_pmx
import itertools as iter

#create a set of random solutions
#param: number of random solutions
#result: set of n random solutions
def init_population(number_of_cities,popultation_size,data):
    cities = get_set_of_cities(number_of_cities,data)
    result = []
    while popultation_size > 0:
        result.append(create_random_start_order(cities))
        popultation_size-=1
    return result

#-----------------------------------------------------------------------
#this function retrurns a random inversion mutation
def inversion_mutation(cities):
    size = len(cities)
    random1 = rand.randint(0,size-1)
    random2 = rand.randint(0,size-1)
    if random1 > random2:
        return inversion_mutation_help(cities,random2,random1)
    else:
        return inversion_mutation_help(cities,random1,random2)
#this function makes the inversion
def inversion_mutation_help(cities,cut1,cut2):
    res = cities.copy()
    index1 = cut2
    index2 = 0
    while index1 >= cut1:
        res[cut1+index2] = cities[index1]
        index1 -=1
        index2 +=1
    return res
#-----------------------------------------------------------------------
#roulette wheel selection
#select lam member of a pool of len(input) individuals
def tournament_selection(input,lam,tournament_size,data):
    res = []

    if lam >= len(input):
        return input,[]
    else:
        while len(res) != lam:
            if tournament_size >= len(input):
                tournament_size = len(input)-1

            tmp_input = input.copy()

            rnd_first = rand.randint(0, len(tmp_input)-1)
            best = tmp_input[rnd_first]
            best_index = rnd_first
            del tmp_input[best_index]

            tur = 1
            #do a torunament with tournament_size members, pick the best one
            #a member can be in a tournement with itself(lower selection pressure)
            while tur < tournament_size:
                rnd_scnd = rand.randint(0, len(tmp_input)-1)
                compare = tmp_input[rnd_scnd]
                if calculate_fitness(compare,data) < calculate_fitness(best,data):
                    best = compare
                    best_index = rnd_scnd
                tur +=1
                del tmp_input[rnd_scnd]
            res.append(best)
            input.remove(best)
    return res,input
#-----------------------------------------------------------------------
#create childs from parents
#do pmx crossover with probaility crossover_rate
def create_childs(cities,crossover_rate):
    vec = np.linspace(0,len(cities)-1,len(cities),dtype=int)
    combinations = list(iter.combinations(vec,2))
    rtrn = []
    for com in combinations:
        rnd = rand.uniform(0,1)
        if rnd <= crossover_rate:
            p1 = cities[com[0]]
            p2 = cities[com[1]]
            res = do_pmx(p1,p2)
            rtrn.append(res[0])
            rtrn.append(res[1])
    return rtrn
#-----------------------------------------------------------------------
#do inversion with probability mutation_rate
def mutation(children, mutation_rate):
    rtrn = []
    for ch in children:
        rnd = rand.uniform(0,1)
        if rnd <= mutation_rate:
            rtrn.append(inversion_mutation(ch))
        else:
            rtrn.append(ch)
    return rtrn

#-----------------------------------------------------------------------
def elitism(input, popultation_size,elite,data):
    if popultation_size > len(input):
        return input
    res = []
    #choose the 'elite' best individuals
    while len(res) < elite:
        elite_res = get_best(input,data)
        if elite_res[0] not in res:
            res.append(elite_res[0])
            input = elite_res[1]

    remaining = popultation_size - elite
    #choose remaining individuals randomly
    while remaining >0:
        random = rand.randint(0, len(input)-1)
        individ = input[random]
        res.append(individ)
        input.remove(individ)
        remaining-=1
    return res

def get_best(cities, data):
    if len(cities) <2:
        return cities[0],[]
    else:
        index = 1
        best_solution = cities[0]
        best_solution_distance = calculate_fitness(best_solution,data)
        while index < len(cities):
            tmp = cities[index]
            tmp_distance = calculate_fitness(tmp,data)
            if tmp_distance < best_solution_distance:
                best_solution = tmp
                best_solution_distance = tmp_distance
            index+=1
        cities.remove(best_solution)
        return best_solution, cities
#-----------------------------------------------------------------------
#functions that extract minumim, maximum and average from a list
def minimum_dist(population,data):
    return np.min(convert(population,data))

def maximum_dist(population,data):
    return np.max(convert(population,data))

def average_dist(population,data):
    return np.average(convert(population,data))

def deviation_dist(population, data):
    return np.std(convert(population,data))

def convert(population,data):
    res = []
    for individual in population:
        res.append(calculate_fitness(individual,data))
    return res

#-----------------------------------------------------------------------

def genetic(number_cities,elite,popultation_size, crossover_rate, mutation_rate,generations,tournament_size,number_tournement_winners):
    data = import_data()
    minimum_generations = []
    #maximum = []
    #average = []
    #deviation = []
    #init the population
    population = init_population(number_cities,popultation_size,data)

    #loop
    index = 1
    while index <= generations:
        #parent selection
        par_selection = tournament_selection(population,number_tournement_winners,tournament_size,data)
        paar = par_selection[0]
        not_paar = par_selection[1]
        #create childs (pmx crossover)
        cross = create_childs(paar, crossover_rate)
        #mutate children (inversion mutation)
        mut = mutation(cross,mutation_rate)
        population = []

        big = not_paar + paar + mut

        #population = not_paar + paar + mut
        population = elitism(big,popultation_size,elite,data)
        tmp = population.copy()
        minimum_generations.append(minimum_dist(tmp,data))
        index+=1

    #maximum.append(maximum_dist(population,data))
    #minimum.append(minimum_dist(population,data))
    #average.append(average_dist(population,data))
    #deviation.append(deviation_dist(population,data))
    return population,minimum_dist(population,data),average_dist(population,data),maximum_dist(population,data),deviation_dist(population,data),minimum_generations


def main():
    data = import_data()
    #parameter:
    #number_of_cities                (eg 6,10,24)
    number_of_cities = 10
    #elite                           ('elite' best individuals will be preserved for the next round)
    elite = 3
    #popultation_size                (number of individuals )
    popultation_size = 4
    #crossover_rate                  (probability to crossover two parents, create two new children)
    crossover_rate = 0.5
    #mutation_rate                   (probability of an inversion_mutation)
    mutation_rate  =0.5
    #generations                     (number of generations that should be simulated)
    generations = 20
    #tournament_size                 (size of the tournaments, higher number means higher selection pressure)
    tournament_size = 2
    #number of tournement winners   (size of the parents that do crossover, after parent selection)
    number_of_tournement_winners = 100

    #print three different generations in one chart
    el = [3,3,3]
    popu = [5,6,7]
    color = ['r','b','g']
    #three_generations(data,number_of_cities,crossover_rate,mutation_rate, generations, tournament_size, number_of_tournement_winners, popu, color, el)

    #do twenty runs on the given parementers obove
    twenty_runs(number_of_cities,
                    elite,
                    popultation_size,
                    crossover_rate,
                    mutation_rate,
                    generations,
                    tournament_size,
                    number_of_tournement_winners,
                    data)




def three_generations(data,
                      number_of_cities,
                      crossover_rate,
                      mutation_rate,
                      generations,
                      tournament_size,
                      number_of_tournement_winners,
                      popu,
                      color,
                      el):
        minimum = []

        main_index = 0
        while main_index < len(popu):
            popultation_size = popu[main_index]
            elite = el[main_index]
            minimum = []
            index = 0
            while index < 20:
                res = genetic(number_of_cities,
                          elite,
                          popultation_size,
                          crossover_rate,
                          mutation_rate,
                          generations,
                          tournament_size,
                          number_of_tournement_winners)
                minimum_generations = res[5]
                minimum.append(minimum_generations)
                index+=1

            #------------------------------------
            print_min = []
            index_out = 0
            while index_out < len(minimum[0]):
                index_in =0
                sum = 0
                while index_in < 20:
                    sum += minimum[index_in][index_out]
                    index_in +=1

                res = sum/len(minimum[0])
                print_min.append(res)
                index_out +=1

            x = np.linspace(1,len(print_min),len(print_min), dtype=int)
            plt.plot(x,print_min,color[main_index], label='Population Size: ' + str(popu[main_index]))
            main_index+=1

        #------------------------------------
        plt.legend(loc='upper right')
        plt.xlabel("Number of Generations")
        plt.ylabel("Fitness")
        plt.savefig("genetic_all_in_one", format="png")
        plt.show()

def twenty_runs(number_of_cities,
                elite,
                popultation_size,
                crossover_rate,
                mutation_rate,
                generations,
                tournament_size,
                number_of_tournement_winners,
                data):
    minimum = []
    maximum = []
    average = []
    deviation = []
    start = timer()

    index = 0
    while index < 20:
        res = genetic(number_of_cities,
                         elite,
                         popultation_size,
                         crossover_rate,
                         mutation_rate,
                         generations,
                         tournament_size,
                         number_of_tournement_winners)
        minimum_generations = res[5]
        minimum.append(minimum_generations)
        average.append(res[2])
        maximum.append(res[3])
        deviation.append(res[4])
        index+=1

        stop = timer()


    #print minimum, average, maximum, deviation
    print("----------Genetic Algorithm----------")
    print("Best individual of each Generation is basic of this statistic.")
    print("Average Time has been determined with", index, "tests.")
    print("Shortest Path (Best case) (Cities", number_of_cities,"):", get_best(res[0],data)[0])
    print("Runtime:"+ "\t"+ "\t", stop-start, "seconds")
    print("Best case:" + "\t"+ "\t", np.min(minimum))
    print("Average case:"+ "\t"+ "\t", np.average(minimum))
    print("Worst case:"+ "\t"+ "\t", np.max(minimum))
    print("Standard deviation:"+ "\t" , np.std(minimum))

main()
