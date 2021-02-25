#Store a list of first names.Count the occurrences of 'a' within the list
name =input("Enter the first names : ")
list = []
count = 0
for x in name:
 list.append(x)
 if(x in name and x == 'a'):
   count = count + 1
print(count)