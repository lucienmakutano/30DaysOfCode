def trailingZeros(number) -> int:
  result  = 1
  counter = 0

  for num in range(1, number + 1 ):
    result = result * num
  
  while result != 0:
    digit = result % 10

    result /= 10

    if digit == 0:
      counter += 1

  return counter


if __name__ == "__main__":
  print(trailingZeros(5))
  print(trailingZeros(3))
  print(trailingZeros(20))
