# Create a single string separated with space from two strings by swapping the character at position 1
def chars_mix_up(a, b):
  str1 = a[0] + b[1] + a[2:]
  str2 = b[0] + a[1] + b[2:]

  return str1 + ' ' + str2
print(chars_mix_up('abc', 'xyz'))