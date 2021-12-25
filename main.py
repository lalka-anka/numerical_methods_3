# coding=utf-8
from algos import gauss
from algos import gauss_main_element_method
from algos import jacobi
from algos import gauss_seidel
from algos import get_same_matrix

if __name__ == '__main__':

    data = [
        [-0.14, 1.21, 1.56, 4.91],
        [0.94, 0.12, -0.61, 1.63],
        [-0.26, -0.50, -0.24, -2.26]
    ]

    print('Метод Гаусса')
    print(gauss(get_same_matrix(data)))
    print("----------------------------------------------------------")

    print('Метод Гаусса с выбором главного элемента')
    print(gauss_main_element_method((get_same_matrix(data))))
    print("----------------------------------------------------------")

    print('Метод Якоби')
    jacobi_matrix = get_same_matrix(data)
    jacobi_matrix[0], jacobi_matrix[1], jacobi_matrix[2] = jacobi_matrix[1], jacobi_matrix[2], jacobi_matrix[0]
    print(jacobi(get_same_matrix(jacobi_matrix))[0])
    print('Число итераций: ', jacobi(get_same_matrix(jacobi_matrix))[1])
    print("----------------------------------------------------------")

    print('Метод Гаусса-Зейделя')
    print(gauss_seidel(get_same_matrix(jacobi_matrix))[0])
    print('Число итераций: ', gauss_seidel(get_same_matrix(jacobi_matrix))[1])
    print("----------------------------------------------------------")
