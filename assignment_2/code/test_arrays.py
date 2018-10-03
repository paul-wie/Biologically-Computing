from array_operations import *

#good
def test_creat_random_array():
    a1 = create_random_array(4,3)
    print(a1)
    print("height:", len(a1))
    print("width:",len(a1[0]))
    print(type(a1))
    print("---------------------")
    a2 = create_random_array(5,7)
    print(a2)
    print("height:", len(a2))
    print("width:",len(a2[0]))
    print(type(a2))



def main():
    test_creat_random_array()


main()
