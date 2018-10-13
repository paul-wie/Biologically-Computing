import numpy as np
from operations import *
from random import shuffle
import matplotlib.pyplot as plt

class mlp:
    def __init__(self, inputs, targets, nhidden):
        self.beta = 1
        self.eta = 0.2
        self.momentum = 0.0
        # type(inputs) = type(targets) = <class 'numpy.ndarray'>
        #so we need numpy to modify the arrays
        # height: 41, width: 12 (nhidden = 12)
        self.weight_matrix_1 = create_random_matrix(len(inputs[0])+1,nhidden)
        #height 13, width: 8 (nhidden =12)
        self.weight_matrix_2 = create_random_matrix(nhidden+1,len(targets[0]))


    def earlystopping(self, inputs, targets, valid, validtargets):
        early_stopping = False
        error_training = []
        error_validation = []
        epochs = 0

        while early_stopping == False:
            rand = self.randomize(inputs, targets)
            inputs = rand[0]
            targets = rand[1]
            error_validation.append(0)
            error_training.append(0)
            iterations = 100
            #-----------------------------------------------------------------------------------
            #training, one iteration through the input data set
            for i in range(iterations):
                for index in range(len(inputs)):
                    target = targets[index]
                    input = inputs[index]
                    forward_results = self.forward(input)
                    hidden_activation = forward_results[0]
                    output_clear = forward_results[1]
                    output_discrete = forward_results[2]
                    output_error = error_output_continious(output_clear,target)
                    hidden_error = self.calculate_hidden_error(output_error,hidden_activation)
                    self.train(input,hidden_activation,hidden_error,output_error)
                    if i == iterations-1:
                        error_training[epochs] += diff_squ_sum_vec_vec(output_clear,target)

            #-----------------------------------------------------------------------------------

            #validation, test early stopping
            errors = 0
            for v,t in zip(valid,validtargets):
                res = self.forward(v)
                error_validation[epochs] += diff_squ_sum_vec_vec(res[1],t)
                errors +=   diff_squ_sum_vec_vec(res[2],t)
            if epochs >1 and error_validation[epochs] > error_validation[epochs-1]:
                early_stopping = True
            epochs +=1
        print("----------------------------------------------------------------------------")
        print("Training Phase")
        print("")
        #print to the console
        print("Training Error  (last iteration of a epoch)  :", error_training)
        print("Validation Error                             :", error_validation)
        print("Number of Epochs                             :", epochs)
        print("Number iterations per epoch                  :",iterations)
        print("Wrong claffifications in validation set:     :", errors)
        print("Percent of Validation Errors                 :",  str((errors/len(valid))*100) + " %")

        #plot result and save it as a pdf file
        x = [ (i+1) for i in range(epochs)]
        plt.plot(x,error_training, 'r', label='Training set (last iteration of a epoch)')
        plt.plot(x,error_validation, 'b',label='Validation set')
        plt.legend(loc='upper right')
        plt.ylabel("Classification Error")
        plt.xlabel("Number of epochs ( " + str(iterations) + " iterations in each epoch)")
        plt.savefig("multi_layer_perceptron.png", format="png")
        #plt.show()
        print("----------------------------------------------------------------------------")


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
            hidden_err[act_index] = hidden_err[act_index] * a * (1-a) * self.beta
        return np.array(hidden_err)

    #runs the network forward.
    #param: input: one input vector
    #return: hidden: activation hidden nodes, output: activation output nodes
    def forward(self, input):
        #add bias
        input = np.append(input,-1)
        hidden_activation = vec_matr_mult(input, self.weight_matrix_1)
        #add bias again
        hidden_activation = np.append(hidden_activation,-1)
        #apply activation function
        hidden_activation = apply_sigmoid_activation(hidden_activation,self.beta)
        #calculate output (activation function: also singmoid
        output = vec_matr_mult(hidden_activation,self.weight_matrix_2)
        #output = apply_sigmoid_activation(output,self.beta)
        return hidden_activation, apply_sigmoid_activation(output,1), convert_output(output)

    def confusion(self, inputs, targets):
        wrong_classifications = 0
        confusion_matrix = build_confusion_matrix(len(targets[0]))

        for inp,tar in zip(inputs,targets):
            res = self.forward(inp)
            wrong_classifications +=   diff_squ_sum_vec_vec(np.copy(res[2]),tar)
            output_index = index_confusion_matrix(np.copy(res[2]))
            target_index = index_confusion_matrix(tar)
            confusion_matrix[target_index][output_index] +=1



        print("Confusion Phase")
        print("")
        print("Number of inputs                 :", len(inputs))
        print("Wrong Classifications            :", wrong_classifications)
        print("Percentage wrong classifications :", str(wrong_classifications/len(inputs)*100) +" %")
        print("-----------------------")
        print("Confusion Matrix")
        print("")
        for row in confusion_matrix:
            print(row)

        print("")
        print("x: Correct classes")
        print("y: Classified classes")
        print("Percentage of correct classes:", str(percetage_correct_classes(confusion_matrix)) + " %")
