n = int(input("Enter a number: "))
e = int(input("Enter exponent: "))
power=1
for i in range(1,e+1):
  power=power*n
print("Power is: ",power)