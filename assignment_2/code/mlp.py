import numpy as np
from array_operations import *

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

        print('To be implemented')



    def earlystopping(self, inputs, targets, valid, validtargets):
        self.train(1,2)
        print('To be implemented')

    def train(self, inputs, targets, iterations=100):
        while iterations > 0:
            print(iterations)
            iterations -=1

        print('To be implemented')

    def forward(self, inputs):
        print('To be implemented')

    def confusion(self, inputs, targets):
        print('To be implemented')
