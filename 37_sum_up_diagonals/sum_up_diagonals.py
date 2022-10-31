def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    for lst in matrix:
        if len(lst) != len(matrix):
            return 'This is not a matrix'
    sum = 0
    for num in range(len(matrix)):
        diagonal_1 = matrix[num][num]
        diagonal_2 = matrix[num][(num + 1) * -1]
        sum = sum + diagonal_1 + diagonal_2
    return sum