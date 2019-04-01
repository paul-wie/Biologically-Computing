#import itertools
import itertools as iter
import numpy as np
import matplotlib.pyplot as plt
from common import *
#import timer
from timeit import default_timer as timer


#this fuction calculates the shortest path for the first "number_cities" cities
def exhaustive_search(number_cities):
    #import the data (implementation: common.py)
    data = import_data()
    #create a set of cities with size of number_cities
    #(implementation: common.py)
    cities = get_set_of_cities(number_cities, data)
    #create a set of all possible permutations
    permutations = list(iter.permutations(cities,number_cities))
    #calculate the result (minimum path length)
    return iterate(permutations,data)


#this function iterates through all permutations
#param: permutations, data
#return: shortest_path and its path length
def iterate(permutations,data):
    index = 1
    shortest_path = permutations[0]
    shortest_distance = calculate_fitness(permutations[0],data)
    while index < len(permutations):
        distance = calculate_fitness(permutations[index],data)
        if distance < shortest_distance:
            shortest_path = permutations[index]
            shortest_distance = distance
        index +=1
    return shortest_path, shortest_distance

#this functions prints the best solution for a specific number of cities
#param: result, set of cities and total distance
#       time, time to find this solution
#       number_cities
def print_console(res, time, number_of_cities):
    print("Shortest Path (Cities:",number_of_cities, "):" ,res[0])
    print("Total Lenght: ",res[1])
    print("Time to find the best solution: ", time, "seconds")

#determines the best solution for one certain number of cities and prints it to the console
def single_solution(number_of_cities):
    start = timer()
    res = exhaustive_search(number_of_cities)
    stop = timer()
    print_console(res,stop-start,number_of_cities)

#this function prints all solutions between 1 and number_of_cities on the console
#it also draws all solution
def plot_several_solutions(number_of_cities):
    if number_of_cities < 1 :
        print("Number of Cities must be bigger than1")
        return -1
    else:
        figure = plt.figure("Exhaustive Search")
        city_vector = np.linspace(1,number_of_cities, number_of_cities)
        results = []
        index = 0
        while index < number_of_cities:
            start = timer()
            res = exhaustive_search(index+1)
            stop = timer()
            results.append((stop-start))
            print_console(res, results[index],index+1)
            print("------------------------------------------------------")
            print("")
            index +=1
        plt.plot(city_vector,results, 'ro')
        plt.xlabel("Number of Cities")
        plt.ylabel("Time to find the best solution (seconds)")
        #plt.savefig("exhaustive_search6.png", format="png")
        plt.show()

#this is the main fuction

def main():
    #change the number of cities
    number_of_cities = 6
    #used to determine several solutions and draw them
    #output: console(shortest paths), pyplot drawing
    plot_several_solutions(number_of_cities)

    #prints one certain solution on the console (uncomment to use it)
    #----------------------------------
    #single_solution(number_of_cities)
    #----------------------------------

main()
