n = int(input())
if (n>2400):
    n = n-2400
print ((n),"in Ottawa")
n-=300
if (n<0):
    n = 2400+n
print ((n),"in Victoria")
n+=100
if (n>2400):
    n = n-2400
print ((n),"in Edmonton")
n+=100
if (n>2400):
    n = n-2400
print ((n),"in Winnipeg")
n+=100
if (n>2400):
    n = n-2400
print ((n),"in Toronto")
n+=100
if (n>2400):
    n = n-2400
print ((n),"in Halifax")
n+=30
if (n>2400):
    n = n-2400
if (n%100 > 59):
    n = n+40
print ((n),"in St. John's")



