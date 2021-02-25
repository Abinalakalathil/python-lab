#3d List ordinal value of each element of a word(Hint:use ord() to get the ordinal values)
w=input("Enter a word : ")
for x in range(len(w)):
  print("ASCII value of" ,w[x] ,"is" ,ord(w[x]))