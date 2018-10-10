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
        

    def earlystopping(self, inputs, targets, valid, validtargets):
        iterations = 100
        forward_res = self.forward(inputs[0])
        activation_hidden_values = forward_res[0]
        output = forward_res[1]
        print(self.weight_matrix_2)
        self.train(inputs[0], targets[0], activation_hidden_values, output)
        print("-------------------------------------------")
        print(self.weight_matrix_2)


    def train(self, input, target, activation_hidden_values, output):
        #calculate output error
        output_err = output_error(convert_output(output), target)
        #update output weights
        self.update_output_weights(self.eta, output_err, activation_hidden_values)
        #calculate hidden error

        #update hidden weights

    def update_output_weights(self,eta, output_err, activation_hidden_values):
        for index_error in range(len(output_err)):
            for index_activation in range(len(activation_hidden_values)):
                self.weight_matrix_2[index_activation][index_error] -= eta*output_err[index_error]*activation_hidden_values[index_activation]



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
