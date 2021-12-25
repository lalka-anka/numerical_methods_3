# coding=utf-8
import math


def gauss(matrix):
    for main_line_number in range(len(matrix) - 1):
        for i in range(main_line_number + 1, len(matrix)):
            line = matrix[i]
            multiplier = line[main_line_number] / matrix[main_line_number][main_line_number]
            line[main_line_number] = 0
            for j in range(main_line_number + 1, len(line)):
                line[j] = line[j] - matrix[main_line_number][j] * multiplier
    roots = []
    for i in range(len(matrix)-1, -1, -1):
        line = matrix[i]
        sum_by_main_matrix_line = 0
        for j in range(len(line) - 2, i, -1):
            sum_by_main_matrix_line += line[j]
        x = (line[len(line) - 1] - sum_by_main_matrix_line) / line[i]
        roots.append(x)

        if i == 0:
            continue
        matrix[i - 1][i] *= roots[len(roots) - 1]

    roots.reverse()
    return roots


def gauss_main_element_method(matrix):
    matrix_copy = get_same_matrix(matrix)

    first = max(matrix_copy, key=lambda line: abs(line[0]))
    matrix_copy.remove(first)
    second = max(matrix_copy, key=lambda line: abs(line[1]))
    matrix_copy.remove(second)
    third = max(matrix_copy, key=lambda line: abs(line[3]))

    new_matrix = [first, second, third]
    roots = gauss(new_matrix)
    return roots


def jacobi(matrix):
    solutions = [tuple((1 for _ in range(len(matrix))))]
    n = 1
    while True:
        new_solution = []
        for i in range(len(matrix)):
            line = matrix[i]
            line_sum = line[len(line) - 1]
            for j in range(len(line) - 1):
                if i == j:
                    continue
                line_sum -= line[j] * solutions[len(solutions)-1][j]
            new_solution.append(line_sum / line[i])

        if check_accuracy(new_solution, solutions[len(solutions) - 1]):
            return new_solution, n

        solutions.append(tuple(new_solution))
        n += 1


def gauss_seidel(matrix):
    solutions = [tuple((1 for _ in range(len(matrix))))]
    n = 1
    while True:
        new_solution = [None for _ in range(len(matrix))]
        for i in range(len(matrix)):
            line = matrix[i]
            line_sum = line[len(line) - 1]
            for j in range(len(line) - 1):
                if i == j:
                    continue
                x_value = solutions[len(solutions) - 1][j] if new_solution[j] is None else new_solution[j]
                line_sum -= line[j] * x_value
            new_solution[i] = line_sum / line[i]

        if check_accuracy(new_solution, solutions[len(solutions) - 1]):
            return new_solution, n

        solutions.append(tuple(new_solution))
        n += 1


def check_accuracy(solution, old_solution):
    difference_sum = sum(((solution[i] - old_solution[i])**2 for i in range(len(solution))))
    return math.sqrt(difference_sum) < 0.5 * 10e-4


def get_same_matrix(matrix):
    matrix_copy = []
    for i in range(len(matrix)):
        line = matrix[i].copy()
        matrix_copy.append(line)
    return matrix_copy

