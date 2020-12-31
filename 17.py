a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if (a>b):
  min=a
else:
  min=b
while (1):
    if (min%a==0 and min%b==0):
         print("LCM is: ",min) 
         break
    min=min+1