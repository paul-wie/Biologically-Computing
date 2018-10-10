from array_operations import *

#good
def test_creat_random_array():
    a1 = create_random_matrix(4,3)
    print(a1)
    print("height:", len(a1))
    print("width:",len(a1[0]))
    print(type(a1))
    print("---------------------")
    a2 = create_random_matrix(4,6)
    print(a2)
    print("height:", len(a2))
    print("width:",len(a2[0]))
    print(type(a2))
#good
def test_vector_matrix_multiplication():
    v1 = np.array([1,2,3])
    m1 = np.array([[1,2,3],
                    [1,2,3],
                    [1,2,3]
                  ])
    print(vec_matr_mult(v1,m1))
    print("---------------------------")
    m2 = create_random_matrix(3,5)
    v2 = np.array([1,2,3])
    res1 = vec_matr_mult(v2,m2)
    res2 = v2.dot(m2)
    print(m2)
    print("Res1:",res1)
    print("Res2:",res2)

#good
def test_activation_function():
    a = [1,1,1]
    b= [1,2,3]
    a1 = activation_hidden(a,1)
    b1 = activation_hidden(b,1)
    print("a", a1, type(a1))
    print("b", b1, type(b1))

def main():
    #test_creat_random_array()
    #test_vector_matrix_multiplication()
    test_activation_function()


main()
