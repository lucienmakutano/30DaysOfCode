def isTriangleNumber(number) -> bool:
  i = 1
  try:
    if number == 0 or number == 1:
      return True

    while number > 0:
      number -= i

      i += 1

    return True if number == 0 else False
    
  except Exception:
    return False

if __name__ == '__main__':
  print(isTriangleNumber(6))
  print(isTriangleNumber(8))
  print(isTriangleNumber(1))
  print(isTriangleNumber(0))
  print(isTriangleNumber(16))
  print(isTriangleNumber(50))
  print(isTriangleNumber(30))
  print(isTriangleNumber(36))
  print(isTriangleNumber(18))
  print(isTriangleNumber(21))
