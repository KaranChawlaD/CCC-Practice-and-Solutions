n = int(input())
m = int(input())
A = []
N = []

for i in range(n):
	A.append(str(input()))
for l in range(m):
	N.append(str(input()))

for j in range(n):
	for k in range(m):
		print (A[j] + " as " + N[k])