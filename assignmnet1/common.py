#this file contains functions that are probably used in several cases
import csv
import random as rand
#define an import data function that is used for all three problems
def import_data():
    with open("european_cities.csv", "r") as f:
        return list(csv.reader(f, delimiter=';'))


#this fuction calculates the total length of one solution
#param: cites, set (list) of european_cities,
#       data, all information concerning the distance
#retrun: total length of this route
def calculate_fitness(cities, data):
    number_of_cities = len(cities)
    if number_of_cities < 2:
        return 0
    else:
        index = 0
        distance = 0
        while (index+1) < number_of_cities:
            distance += get_distance(cities[index], cities[index+1],data)
            index +=1
        distance += get_distance(cities[number_of_cities-1],cities[0],data)
        return distance

#this function returns a citys index concerning
#param: city,data
#return: index of the city
def get_index(city,data):
    all_cities = data[0]
    index = 0
    while index < len(all_cities):
        if city == all_cities[index]:
            return index
        index +=1
    return -1


#this function returns the distance between two cities
#param: city1, city2, data
#return: distance between these two cities
def get_distance(city1, city2,data):
    index1 = get_index(city1, data)
    index2 = get_index(city2, data)
    #index+1, because the first array of the array is the one with the citiy names
    return float(data[index1+1][index2])

#this function extracts cities from the data
#param: amount, number of cities to extract, data
#return: a set of cities that has size of size
def get_set_of_cities(size, data):
    result = []
    index = 0
    all_cities = data[0]
    while index < size:
        result.append(all_cities[index])
        index +=1
    return result


#This function takes a set of cities and mix the order
#param: cities, a set of cities
#return: a set of cities, random order
def create_random_start_order(cities):
    number_of_cities = len(cities)
    new_order = [''] * number_of_cities
    index = 0
    while index < len(cities):
        random = rand.randint(0,number_of_cities-1)
        while new_order[random] != '':
            random = rand.randint(0,number_of_cities-1)
        new_order[random] = cities[index]
        index+=1
    return new_order
