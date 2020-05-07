def product2Sum(array1, array2) -> int:
  total = 0

  if len(array1) != len(array2):
    return -1

  for i in range(0, len(array1)):
    total += array1[i] * array2[i]

  return total 

if __name__ == '__main__':
  print(product2Sum([2, 6, 9, 4], [1, 2, 4, 8]))
  print(product2Sum([0, 0, 0, 0], [1, 2, 4, 8]))
  print(product2Sum([2, 0, 3, 7], [5, 1, 2, 3])) # 37
  print(product2Sum([1, 1, 9, 4], [1, 2, 4, 2])) # 47
