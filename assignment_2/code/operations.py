import numpy as np
import sys
import random as rand
import math
#--------------------------------------------------------------
#create a random array with dimension og height and width
def create_random_matrix(height, width):
    output = []
    for index1 in range(height):
        new_row = []
        for index2 in range(width):
            new_row.append(rand.uniform(-1,1))
        output.append(new_row)
    return np.array(output)

#--------------------------------------------------------------
#vector matrix multiplication
def vec_matr_mult(vec,matr):
    if len(vec) != len(matr):
        print("Vector and matrix do not have the same dimension")
        sys.exit(0)
    else:
        output = np.zeros(len(matr[0]))
        for index in range(len(matr[0])):
            for mul in range(len(vec)):
                output[index] += vec[mul]*matr[mul][index]
        return output

#--------------------------------------------------------------
#activation function
def activation_hidden(values,beta):
    for i in range(len(values)):
        values[i] = activation_function(values[i],beta)
    return np.array(values)

def activation_function(x,beta):
    return 1 / (1+ math.exp(-beta*x))
#--------------------------------------------------------------
#convert output vector with continious values to an output with 0 and one 1
def convert_output(output):
    maximum = max(output)
    ret = [0] * len(output)
    for i in range(len(output)):
        if output[i] == maximum:
            ret[i] = 1
    return ret
#--------------------------------------------------------------
# calculate output error
def output_error(actual_output, aim_output):
    for i in range(len(actual_output)):
        actual_output[i] = actual_output[i]- aim_output[i]
    return actual_output
