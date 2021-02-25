#Print out all colors from color_list1 not contained in color_list2
color_list1 = set(["Red" , "Blue" , "White"])
color_list2 = set(["White" , "Black","Green"])
print(color_list1.difference(color_list2))