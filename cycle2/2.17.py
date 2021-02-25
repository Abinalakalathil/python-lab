#Sort dictionary in ascending and descending order
y={'vyshu':50,'dona':27,'athira':49,'keerthi':89}
print("Original dictionary : " , y)
l=list(y.items())
l.sort()
print("Ascending order : " , l)
l=list(y.items())
l.sort(reverse=True)
print("Descending order : " , l)