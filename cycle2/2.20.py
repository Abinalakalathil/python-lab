#From a list of integers create new list removing even numbers
list =[11,7,56,78,13]
print("Original list:",list)
for i in list:
  if (1%2 == 0):
       list.remove(i)
print("List After removing  Even Numbers:",list)