year = int(input("Enter the year: "))
if (year % 4) == 0:
 if (year % 100) == 0:
  if (year % 400) == 0:
      print("{0} is Leapyear".format(year))
  else:
    print("{0} is not Leapyear".format(year))
 else:
    print("{0} is Leapyear".format(year)) 
else:
    print("{0} is not Leapyear".format(year))