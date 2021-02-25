# Get a string from an i/p string where all occurrences of 1st character replaced with '$',except 1st character
def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]
  return str1
print(change_char('italic'))