def dynamic_matrix_multiplication_memoization(arr, i, j, result_array):
    if (i == j):
        return 0

    if (result_array[i][j] != -1):
        return result_array[i][j]

    result_array[i][j] = float('inf')

    for k in range(i, j):
        result_array[i][j] = min(result_array[i][j], dynamic_matrix_multiplication_memoization(arr, i, k,
                                                                                               result_array) + dynamic_matrix_multiplication_memoization(
            arr, k + 1, j, result_array) + arr[i - 1] * arr[k] * arr[j])

    return result_array[i][j]


arr = [30,35,15,5,10,20,25]
n = len(arr)
i = 1
j = n - 1
result_array = [[-1 for i in range(n)] for j in range(n)]
print("Minimum number of multiplications is:", dynamic_matrix_multiplication_memoization(arr, i, j, result_array))