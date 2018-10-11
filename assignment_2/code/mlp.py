import numpy as np
from operations import *
from random import shuffle
class mlp:
    def __init__(self, inputs, targets, nhidden):
        self.beta = 1
        self.eta = 0.5
        self.momentum = 0.0
        # type(inputs) = type(targets) = <class 'numpy.ndarray'>
        #so we need numpy to modify the arrays
        # height: 41, width: 12 (nhidden = 12)
        self.weight_matrix_1 = create_random_matrix(len(inputs[0])+1,nhidden)
        #height 13, width: 8 (nhidden =12)
        self.weight_matrix_2 = create_random_matrix(nhidden+1,len(targets[0]))


    def earlystopping(self, inputs, targets, valid, validtargets):

        epochs = 30
        failure = [0] * epochs
        for epoch in range(epochs):
            rand = self.randomize(inputs, targets)
            inputs = rand[0]
            targets = rand[1]
            for index in range(len(inputs)):
                target = targets[index]
                input = inputs[index]

                forward_results = self.forward(input)
                hidden_activation = forward_results[0]
                output_clear = forward_results[1]
                output_discrete = forward_results[2]
                output_error = calculate_output_error(output_discrete,target)
                hidden_error = self.calculate_hidden_error(output_error,hidden_activation)
                self.train(input,hidden_activation,hidden_error,output_error)
                failure[epoch] += self.check_failure(output_discrete,target)
        print(failure)

        output_fail = 0
        for v,t in zip(valid,validtargets):
            res = self.forward(v)
            discrete_output = res[2]
            output_fail += self.check_failure(discrete_output,t)

        print("inputs", len(valid))
        print("failed output:",output_fail)

    #check if a output is equal to the target output
    def check_failure(self,output,target):
        for v1,v2 in zip(output,target):
            if v1!=v2:
                return 1
        return 0

    #randomize the input data to avoid same train order for all iterations
    def randomize(self, inputs, targets):
        ret_inputs = [[]] * len(inputs)
        ret_targets = [[]] * len(targets)
        new_order = [i for i in range(len(inputs))]
        shuffle(new_order)
        for index in range(len(inputs)):
            ret_inputs[new_order[index]] = inputs[index]
            ret_targets[new_order[index]] = targets[index]
        return ret_inputs, ret_targets

    #train the network, to the backpropagation
    def train(self, input, activation_hidden_values,hidden_error, output_error,):
        self.update_weights(self.eta, output_error, activation_hidden_values, self.weight_matrix_2)
        self.update_weights(self.eta, hidden_error, input, self.weight_matrix_1)


    #update weight of the given layer depentding on an output error and a perceptron activation
    def update_weights(self,eta, error, activation, weight_matrix):
        for act_index in range(len(activation)):
            for err_index in range(len(error)):
                weight_matrix[act_index][err_index] -= eta * activation[act_index] * error[err_index]


    #calculate the error for all hidden nodes depending on output errors and weights
    def calculate_hidden_error(self, output_err, activation_hidden_values):
        hidden_err = [0] * (len(activation_hidden_values)-1)
        for act_index in range(len(hidden_err)):
            a = activation_hidden_values[act_index]
            for err_index in range(len(output_err)):
                hidden_err[act_index] += output_err[err_index]*self.weight_matrix_2[act_index][err_index]
            hidden_err[act_index] = hidden_err[act_index] * a * (1-a)
        return np.array(hidden_err)

    #runs the network forward.
    #param: input: one input vector
    #return: hidden: activation hidden nodes, output: activation output nodes
    def forward(self, input):
        #add bias
        input = np.append(input,-1)
        hidden_values = vec_matr_mult(input, self.weight_matrix_1)
        #add bias again
        hidden_values = np.append(hidden_values,-1)
        #apply activation function
        hidden_values = apply_sigmoid_activation(hidden_values,self.beta)
        #calculate output (activation function: also singmoid
        output = vec_matr_mult(hidden_values,self.weight_matrix_2)
        #output = apply_sigmoid_activation(output,self.beta)
        return hidden_values,output, convert_output(output)

    def confusion(self, inputs, targets):
        print('To be implemented')
