#7b check whether lists sums to same value
list1 = [1, 2, 4, 4, 8] 
list2 = [1, 2, 4, 5] 
print ("The first list is : " + str(list1)) 
print ("The second list is : " + str(list2)) 
sum1 = 0
sum2 = 0
for x in range(0, len(list1)):
    sum1 = sum1 + list1[x]
print("Sum of all elements in given list1 : ", sum1)
for x in range(0, len(list2)):
    sum2 = sum2 + list2[x]
print("Sum of all elements in given list2 : ", sum2)    
if( sum1 == sum2):
  print("Lists sums to same value")
else:
  print("Lists sums to different value")