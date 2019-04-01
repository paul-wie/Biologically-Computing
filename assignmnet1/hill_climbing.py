from common import *
from timeit import default_timer as timer
import numpy as np
import as rand
import itertools as iter
import sys


#mainimizes the route length of a random route by swapping pairs of cities
def hill_climbing(number_of_cities):
    data = import_data()
    cities = get_set_of_cities(number_of_cities,data)
    #create a random route
    best_solution = create_random_start_order(cities)
    best_solution_distance = calculate_fitness(best_solution,data)
    #get all possible swaps
    combinations = get_combinations(best_solution)
    index = 0
    while index < len(combinations):
        pair = combinations[index]
        swapped_solution = swap_two_cities(pair,best_solution)
        swapped_solution_distance = calculate_fitness(swapped_solution,data)
        if swapped_solution_distance < best_solution_distance:
            best_solution = swapped_solution
            best_solution_distance = swapped_solution_distance
            #recalculate all possible swaps
            combinations = get_combinations(best_solution)
            index = 0
        else:
            index +=1
    return best_solution,best_solution_distance

#executes the hill_climbing() several times. Return all important information
def execute_hill_climber(number_of_cities,number_of_tests):

    time_table = [0] * number_of_tests
    distance_table = [0] * number_of_tests

    best_solution = []
    best_solution_distance = sys.maxsize

    index = 0
    while index < number_of_tests:
        start = timer()
        res = hill_climbing(number_of_cities)
        stop = timer()

        sol_dist = res[1]
        distance_table[index] = sol_dist
        time_table[index] = stop-start

        if sol_dist < best_solution_distance:
            best_solution = res[0]
            best_solution_distance = sol_dist

        index +=1

    return best_solution,best_solution_distance,distance_table,time_table
#executes hill_climbing several times and prints the result to the console
def print_hill_climber(number_of_cities,number_of_tests):
    res = execute_hill_climber(number_of_cities,number_of_tests)
    best_solution = res[1]
    time_table = res[3]
    print("Average Time has been determined with", number_of_tests, "tests.")
    print("Shortest Path (Best case) (Cities", number_of_cities,"):", res[0])
    print("Average Time:"         + "\t"+ "\t",np.average(time_table), " seconds")
    print("Best case:"            + "\t" + "\t", res[1])
    print("Worst case:"           + "\t" + "\t", np.amax(res[2]))
    print("Average:"              + "\t" + "\t", np.average(res[2]))
    print("Standard deviation:"   + "\t", np.std(res[2]))

def main():
    #number of cities
    number_of_cities = 24
    #number of runs that should be done
    number_of_tests = 1
    print_hill_climber(number_of_cities, number_of_tests)

#retruns all possible swap combinations
def get_combinations(cities):
    return list(iter.combinations(cities,2))

#swaps two cities
def swap_two_cities(pair, cities):
    #put the cities in a list so the function get_index can be reused
    pack = [cities]
    index1 = get_index(pair[0],pack)
    index2 = get_index(pair[1],pack)

    tmp = cities[index1]
    cities[index1] = cities[index2]
    cities[index2] = tmp
    return cities



main()
