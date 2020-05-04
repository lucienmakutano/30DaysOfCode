def confusedString(string) -> str:
  try:
    if len(string) == 0:
      return 'empty string'

    return string.upper() + ', ' + string.lower()

  except  Exception:
    return "not a string"

if __name__ == '__main__':
  print(confusedString('HasTaLAvisTA'))
  print(confusedString('AAAAAA'))
  print(confusedString('aaaaa'))
  print(confusedString('DbSbAhDoDfDD'))
  print(confusedString(''))
  print(confusedString(1))
