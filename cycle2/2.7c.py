#7c check whether any value occur in both
list1 = [10, 20, 40, 3, 8] 
list2 = [1, 2, 4, 3, 5] 
print ("The first list is : " + str(list1)) 
print ("The second list is : " + str(list2)) 
print("The values occur in both lists : ")
for x in list1:
  if(x in list1 and x in list2):
    print(x)