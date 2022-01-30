temp = True
counter = 0
T = []
A = []
while (temp == True):
    counter += 1
    if (counter%2 == 1):
        T.append(str(input()))
    elif (counter%2 == 0):
        A.append(str(input()))
        if (A[counter//2 - 1] == "SCHOOL"):
            temp = False
T.reverse()
A.reverse()
A.remove(A[0])
A.append("HOME.")
for l in range(0, len(T)):
    if T[l]=="L":
        T[l]="RIGHT"
    elif T[l]=="R":
        T[l]="LEFT"
for k in range(1, len(A)+1):
    if (k==len(A)):
        print ("Turn", (T[k-1]), "into your", (A[k-1]))
    if (k != len(A)):
        print ("Turn", (T[k-1]), "onto", (A[k-1]), "street.")