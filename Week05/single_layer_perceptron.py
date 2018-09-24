













main():
    data_and = [    #bias   i1  i2  y
                    [1,   0,  0,  0],
                    [1,   1,  0,  0],
                    [1,   0,  1,  0],
                    [1,   1,  1,  1]
                ]
    weight = [-1.5,1,1]
    print(zip(data_and,weight))



if __name__ == '__main__':
    main()
