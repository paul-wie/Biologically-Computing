import itertools

#hidden functions
def hidden():
    add = lambda x,y: x+y
    #3
    print(add(1,2))

#list slice
def list_slice():
    a = [1,2,3,4,5,6,7]
    #[2]
    print(a[1:2])

def negative_index():
    a = [1,2,3,4,5]
    #5
    print(a[-1])
    #4
    print(a[-2])

def loop1():
    #0, 1, 2, 3, 4,
    for i in range(0,5,1):
        print(i)

def loop2():
    a=[1,2,3,4,5,6]
    for i in range(len(a)):
        #[1,2,3,4,5,6]
        print(a[i])



loop2()
