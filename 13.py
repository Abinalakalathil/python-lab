a=int(input("Enter a Number\n"))
fact=1
if (a < 0):
  print("Factorials does not exist for negative number")
elif (a == 0):
  print("Factorial of 0 is 1")
else:
  for i in range(1,a + 1):
    fact=fact*i
  print("Factorial of",a,"is",fact)