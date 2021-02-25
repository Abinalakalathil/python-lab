#Merge 2 dictionaries
dict1={"a":100,"b":200}
dict2={"c":300,"d":400}
newdict=dict1.copy()
newdict.update(dict2) 
print("Merged dictionary:",newdict)