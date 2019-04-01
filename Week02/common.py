

def proof(par1,par2,cut1,cut2):
    if len(par1) != len(par2):
        print("Parents do not have the same length")
        return [-1]
    elif cut1 > cut2:
        print("Cut1 must be smaller than Cut2")
        return [-1]
    elif cut2 >= len(par1):
        print("Cut2 must be smaller than Parent1 length")
        return [-1]
    elif cut2 >= len(par2):
        print("Cut2 must be smaller than Parent2 length")
        return [-1]

def short_proof(parent1,parent2):
    proof(parent1, parent2,0,0)


#returns the index of a number in a list
def locate(par,value):
    index = 0
    max = len(par)
    while index < max:
        if par[index] == value:
            return index
        index += 1
#1: number has already been copied
#0: number hasn't been copied
def number_already_copied(par, number, cut1, cut2):
    while cut1 <= cut2:
        if par[cut1] == number:
            return 1
        cut1 +=1
    return 0

def create_empty_array(length):
    index =0
    arr = []
    while index < length:
        arr.append(0)
        index +=1
    return arr
