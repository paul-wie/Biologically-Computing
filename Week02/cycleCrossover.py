from common import *






def cycle_crossover(parent1, parent2):
    short_proof(parent1,parent2)

    child = create_empty_array(len(parent1))
    child =cycle(parent1,parent2,child,0)

    #child = cycle(parent2,parent1,child,0)
    print(child)


def cycle(parent1, parent2,child,start):
    starting_index = start
    starting_number = parent1[starting_index]
    next_number = parent2[starting_index]


    child[starting_index] = parent1[starting_index]
    while starting_number != next_number:
        next_number_index = locate(parent1, next_number)
        next_number = parent2[next_number_index]
        child[next_number_index] = parent1[next_number_index]
    return child










p1 = [1,2,3,4,5,6,7,8,9]
p2 = [9,3,7,8,2,6,5,1,4]

r1 = [2,4,7,1,3,6,8,9,5]
r2 = [5,9,8,6,2,4,1,3,7]
cycle_crossover(r1,r2)
