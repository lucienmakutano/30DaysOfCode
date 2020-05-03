def localSant(numOfSiblings, numOfSweets) -> str:

  try:
    if numOfSweets == 0:
      return 'no sweets left'

    if numOfSweets % numOfSiblings == 0:
      return 'give away'
    else:
      return 'eat them yourself'

  except ZeroDivisionError:
    return 'eat them yourself'


if __name__ == '__main__':
  print(localSant(3, 81)) # give away
  print(localSant(3, 8))  # eat them yourself
  print(localSant(3, 0))  # no sweets left
  print(localSant(0, 18)) # no siblings to share with
