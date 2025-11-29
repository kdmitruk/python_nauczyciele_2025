def knapsack(k, values, weights):
  if k == 0:
    return 0
  elif k > sum(weights):
    return sum(values)
  else:
    n = len(values)
    array = [(k + 1) * [0] for i in range(n)]
    for j in range(weights[0], k + 1):
      array[0][j] = values[0]
    for i in range(1, n):
      for j in range(k + 1):
        if weights[i] > j:
          array[i][j] = array[i - 1][j]
        else:
          array[i][j] = max(array[i - 1][j], array[i - 1][j - weights[i]] + values[i])
    return array[n - 1][k]

values = [20, 30, 15, 25, 10]
weights = [6, 13, 5, 10, 3]
k = 20

print(knapsack(k, values, weights))