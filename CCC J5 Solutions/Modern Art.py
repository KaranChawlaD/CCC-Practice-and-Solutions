M = int(input())
N = int(input())

Row_M = []
Column_N = []
Count = 0

for q in range(M):
    Row_M.append(0)
for p in range(N):
    Column_N.append(0)

K = int(input())

for _ in range (K):
    Input = input().split()

    if Input[0] == "R":
        Row_M[int(Input[1]) -1] += 1

    if Input[0] == "C":
        Column_N[int(Input[1]) -1] += 1

for q in range(M):
    for p in range(N):
        Count += (Row_M[q] + Column_N[p]) % 2

print (Count)