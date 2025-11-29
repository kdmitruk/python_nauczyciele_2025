def knapsack(k, i, values, weights, lookup=None):
  lookup = {} if lookup is None else lookup
  if (k,i) in lookup:
    return lookup[(k,i)]
  if i == len(values):
    return 0
  elif weights[i] > k:
    temp = knapsack(k, i+1, values, weights)
    lookup[(k,i)]=temp
    return temp
  else:
    temp = max(values[i] + knapsack(k - weights[i], i + 1, values, weights),
               knapsack(k, i + 1, values, weights))
    lookup[(k,i)]=temp
    return temp


values = [20, 30, 15, 25, 10]
weights = [6, 13, 5, 10, 3]
k = 20

knapsack(k, 0, values, weights)