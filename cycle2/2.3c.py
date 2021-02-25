#Forn a list of vowels selected from a given word
a=input("Enter a Word:")
vowels=["a" , "e" , "i" , "o" , "u"]
list=[]
for x in a:
  if(x in vowels and x not in list):
    list.append(x)
print("Vowels in the given word : " , list)