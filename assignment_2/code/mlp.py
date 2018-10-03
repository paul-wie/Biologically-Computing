import numpy as np

class mlp:
    def __init__(self, inputs, targets, nhidden):
        self.beta = 1
        self.eta = 0.1
        self.momentum = 0.0
        # type(inputs) = type(targets) = <class 'numpy.ndarray'>
        #so we need numpy to modify the arrays
        

        print('To be implemented')



    def earlystopping(self, inputs, targets, valid, validtargets):

        print('To be implemented')

    def train(self, inputs, targets, iterations=100):
        print('To be implemented')

    def forward(self, inputs):
        print('To be implemented')

    def confusion(self, inputs, targets):
        print('To be implemented')
