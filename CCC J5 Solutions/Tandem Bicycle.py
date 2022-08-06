Option = int(input())

N = int(input())

D = input().split()
P = input().split()

Output = 0

for l in range(N):
    D[l] = int(D[l])
    P[l] = int(P[l])

D.sort()
P.sort()

if Option == 1:
    for q in range(N):
        Output += max(D[q], P[q])

if Option == 2:
    for q in range(N):
        Output += max(D[q], P[N-q-1])
        
print(int(Output))