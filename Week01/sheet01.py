import numpy as np
import matplotlib.pyplot as plt
import random as rnd

#Plotting
def f(x):
    return -x**4 + 2*x**3 + 2*x**2 -x

def df(x):
    return -4*x**3 + 6*x**2 + 4*x -1

x = np.linspace(-2,3,1000)

def doPlot():
    fig = plt.figure("Biologically Inspired Computing")
    fig.suptitle("Function and its dervirative")
    plt.subplot(211)
    plt.plot(x,f(x))
    plt.subplot(212)
    plt.plot(x,df(x))
    plt.show()


#Gradient Ascent

def gradient_ascent(f, df, x,gamma, precision):
    dx = gamma * df(x)
    plt.plot(x, f(x),'bo')
    while abs(dx) > precision:
        x += dx
        plt.plot(x, f(x),'ro')
        dx = gamma * df(x)
    return x, f(x)

def draw_gradient_ascent(function, derivative, start, stop, steps):
    fig = plt.figure("Gradient ascent")
    plt.figure("Gradient ascent")
    x = np.linspace(start,stop,steps)
    plt.subplot(211)
    plt.plot(x,f(x))
    res = gradient_ascent(f, df, 0.1, 0.1, 0.01)
    plt.plot(res[0],res[1], 'go', markersize=8)
    plt.subplot(212)
    plt.plot(x,df(x))
    plt.show()


def exhaustive_search(fun,start, stop, delta):
    maximumY = fun(start)
    maximumX = start
    fig = plt.figure("Exhaustive Search")
    plt.plot(start, fun(start), 'bo')

    start += delta
    while start <= stop:
        if(fun(start) > maximumY):
            maximumY = fun(start)
            maximumX = start
        plt.plot(start, fun(start), 'bo')
        start += delta

    plt.plot(maximumX, maximumY, 'ro', markersize=10)
    plt.savefig("exhaustive_search.pdf", format="pdf")
    plt.show()

#exhaustive_search(f,-2,3,0.5)
exhaustive_search(f,-2,3,0.2)
