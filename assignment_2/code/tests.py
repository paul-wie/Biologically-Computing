from operations import *
from random import shuffle
import numpy as np
#-----------------------------------------------------------
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
#-----------------------------------------------------------
#good
def test_vector_matrix_multiplication():
    v1 = np.array([1,2,3])
    m1 = np.array([[1,2,3],
                    [1,2,3],
                    [1,2,3]
                  ])
    res = vec_matr_mult(v1,m1)
    print(res)
    print(len(res))
    print("---------------------------")
    m2 = create_random_matrix(3,5)
    v2 = np.array([1,2,3])
    res1 = vec_matr_mult(v2,m2)
    res2 = v2.dot(m2)
    print(m2)
    print("Res1:",res1)
    print("Res2:",res2)
#-----------------------------------------------------------
#good
def test_activation_function():
    a = [1,1,1]
    b= [1,2,3]
    a1 = activation_hidden(a,1)
    b1 = activation_hidden(b,1)
    print("a", a1, type(a1))
    print("b", b1, type(b1))
#-----------------------------------------------------------
#good
def test_convert_output():
    a1 = [-0.234,0,3.234567,1.99,3.23456]
    print(a1)
    print(convert_output(a1))
#-----------------------------------------------------------
# good
def test_output_error():
    out1 = [0,0,0,1,0,0]
    out2 = [0,0,0,1,0,0]
    out3 = [1,0,0,0,0,0]
    out4 = [0,0,0,1,0,0]
    print(output_error(out1,out2))
    print(output_error(out4,out3))
#-----------------------------------------------------------
#good
def test_calculate_output_error():
    a = [1,0,0,0]
    b = [0,0,0,1]
    print(calculate_output_error(a,b))
#-----------------------------------------------------------
#good
def test_difference_vec_vec():
    v1 = [0,1,0]
    v2 = [1,0,0]
    v3 = [0,1,0]

    #res1 = difference_vec_vec(v1,v2)
    res2 =difference_vec_vec(v1,v3)

    #print(res1)
    print(res2)
#-----------------------------------------------------------
#bassd
def test_diff_squ_sum_vec_vec():
        v1 = [0,1,0]
        v2 = [1,0,0]
        v3 = [0,1,0]

        res1 = diff_squ_sum_vec_vec(v1,v2)
        #res2 = diff_squ_sum_vec_vec(v1,v3)

        print(res1)
        #print(res2)
#-----------------------------------------------------------
#good
def test_build_confusion_matrix():
    c1 = build_confusion_matrix(8)
    print("Height   :",len(c1))
    print("Width    :",len(c1[0]))
    for row in c1:
        print(row)
#-----------------------------------------------------------
#good
def test_index_confusion_matrix():
    vec1 = [0,0,0,1,0,0,0]
    vec2 = [0,0,0,0,0,0,1]

    print(index_confusion_matrix(vec1),3)
    print(index_confusion_matrix(vec2),6)

def main():
    #test_creat_random_array()
    #test_vector_matrix_multiplication()
    #test_activation_function()
    #test_convert_output()
    #test_output_error()
    #test_calculate_output_error()
    #test_difference_vec_vec()
    #test_diff_squ_sum_vec_vec()
    #test_build_confusion_matrix()
    test_index_confusion_matrix()

main()
