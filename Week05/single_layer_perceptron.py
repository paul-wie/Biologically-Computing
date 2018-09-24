
from matplotlib import pyplot as plt
import numpy as np
from write_to_file import *

def plot_wrong_outputs(wrong_outputs,show_figure,filename):
    x = np.linspace(1,len(wrong_outputs),len(wrong_outputs))
    plt.plot(x,wrong_outputs)
    plt.savefig(filename+".png", format="png")
    plt.title(filename)
    plt.xlabel("Epoches")
    plt.ylabel("Wrong Outputs")
    if show_figure:
        plt.show()


#predict the output for a specific input sequence
def predict(inputs,weights):
    threshold = 0.0
    activation = 0.0
    for input,weight in zip(inputs, weights):
        activation += input*weight
    return 1.0 if activation >= threshold else 0

#recalculate weights
def recalculate_weights(inputs,weights):
    new_weights = []
    learning_rate = 0.25
    for input,weight in zip(inputs,weights):
        new_weight = weight+ learning_rate*(inputs[3]-predict(inputs,weights))*input
        new_weights.append(new_weight)
    return new_weights

#train the perceptron by adapting the weight in several epochs
def train(matrix, weights,nu_epoch,filename):
    file = open(filename,"w")
    wrong_outputs = [0] * nu_epoch
    for epoch in range(nu_epoch):
        write_begin(file,epoch)
        for data_set in matrix:
            output = predict(data_set,weights)
            write_it(file,data_set, weights,output, data_set[3])
            if output !=data_set[3]:
                wrong_outputs[epoch] += 1
                weights = recalculate_weights(data_set,weights)

        write_end(file,wrong_outputs[epoch])
    file.close()
    plot_wrong_outputs(wrong_outputs,False,filename)


def main():
    data_and = [    #bias   i1  i2  y
                    [1.00,   0.00,  0.00,     0.00],
                    [1.00,   1.00,  0.00,     0.00],
                    [1.00,   0.00,  1.00,     0.00],
                    [1.00,   1.00,  1.00,     1.00]
                ]
    weights = [2.00,1.00,1.00]
    nu_epoch = 10
    filename = "and_perceptron_"+str(nu_epoch)
    train(data_and,weights, nu_epoch, filename)



if __name__ == '__main__':

    main()
