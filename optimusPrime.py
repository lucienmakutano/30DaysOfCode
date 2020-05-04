def optimusPrime(number) -> list:
  primes = []
  maxRange = number + 1

  if number <= 1:
    return primes

  for num in range(2, maxRange):
    if num % 2 != 0:
      primes.append(num)

  return primes

if __name__ == '__main__':
  print(optimusPrime(11))
  print(optimusPrime(10))
  print(optimusPrime(100))
  print(optimusPrime(1))
  print(optimusPrime(0))
