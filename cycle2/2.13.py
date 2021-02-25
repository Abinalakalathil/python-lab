#13 Create a list of colors from comma-separated color name entered by user.Display 1st & last color
word = input("Enter the colors : ")
color_list = word.split(",")
print("The color list is : " , color_list)
print("The first and last colors are : ")
print( "%s %s"%(color_list[0],color_list[-1]))