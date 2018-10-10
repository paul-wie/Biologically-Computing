import numpy as np
from operations import *

class mlp:
    def __init__(self, inputs, targets, nhidden):
        self.beta = 1
        self.eta = 0.1
        self.momentum = 0.0
        # type(inputs) = type(targets) = <class 'numpy.ndarray'>
        #so we need numpy to modify the arrays
        # height: 41, width: 12 (nhidden = 12)
        self.weight_matrix_1 = create_random_matrix(len(inputs[0])+1,nhidden)
        #height 13, width: 8 (nhidden =12)
        self.weight_matrix_2 = create_random_matrix(nhidden+1,len(targets[0]))

        a =self.forward(inputs[0])
        print(a[0])
        print(a[1])

    def earlystopping(self, inputs, targets, valid, validtargets):
        print("Impement itttttt!!!")

    def train(self, inputs, targets, iterations=100):
        print("iterations", iterations)



    #runs the network forward.
    #param: input: one input vector
    #return: hidden: activation hidden nodes, output: activation output nodes
    def forward(self, input):
        #add bias value -1
        input = np.append(input,-1)
        hidden_values = vec_matr_mult(input,self.weight_matrix_1)
        activation_hidden_values = activation_hidden(hidden_values,self.beta)
        #add bias value -1
        activation_hidden_values = np.append(activation_hidden_values,-1)
        output = vec_matr_mult(activation_hidden_values,self.weight_matrix_2)
        return activation_hidden_values, output

    def confusion(self, inputs, targets):
        print('To be implemented')
