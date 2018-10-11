import numpy as np
import sys
import random as rand
import math
#some functions are implemented in operations.py to test them easily
#--------------------------------------------------------------
#create a random array with dimension og height and width
def create_random_matrix(height, width):
    output = []
    for index1 in range(height):
        new_row = []
        for index2 in range(width):
            new_row.append(rand.uniform(0,1))
        output.append(new_row)
    return np.array(output)

#--------------------------------------------------------------
#vector matrix multiplication
def vec_matr_mult(vec,matr):
    output = np.zeros(len(matr[0]))
    for index in range(len(matr[0])):
        for mul in range(len(vec)):
            output[index] += vec[mul]*matr[mul][index]
    return output

#--------------------------------------------------------------
#activation function
def apply_sigmoid_activation(values,beta):
    for i in range(len(values)):
        values[i] = activation_function(values[i],beta)
    return np.array(values)
#works fine
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
    return np.array(ret)
#--------------------------------------------------------------
# calculate output error
def calculate_output_error(actual_output, aim_output):
    y = np.copy(actual_output)
    t = np.copy(aim_output)
    for i in range(len(y)):
        y[i] = y[i]- t[i]
    return np.array(y)