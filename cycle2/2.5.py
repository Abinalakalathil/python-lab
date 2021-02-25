#Prompt the user for a list of integers.For all values > 100 store 'over' instead
x=[]
n=int(input("How many integers you want to enter :"))
print("Enter integers : ")
for i in range(1,n+1):
  a=int(input())
  if(a>100):
    x.append('over')
  else:
    x.append(a)
print("New list : " , x)