def isPalindrome(str) -> bool:
  letters = [letter for letter in str]
  head = 0
  tail = len(letters) - 1

  if len(letters) == 0:
      return False

  while (head < tail):
      if letters[head] != letters[tail]:
          return False

      head = head + 1
      tail = tail - 1

  return True


if __name__ == '__main__':
  print(isPalindrome("mam".lower()))
