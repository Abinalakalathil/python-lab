#a) check whether lists are of same length
list1 = [1, 2, 4, 3, 8] 
list2 = [1, 2, 4, 3, 5] 
print ("The first list is : " + str(list1)) 
print ("The second list is : " + str(list2)) 
l1 = len(list1)
l2 = len(list2)
print("Length of list1 : " , l1 , "and Length of list2 : " , l2)
if l1 == l2: 
    print ("The lists are of same length") 
else : 
    print ("The lists are of different length")