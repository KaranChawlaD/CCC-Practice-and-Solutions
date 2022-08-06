A = int(input())
B = int(input())

listy = [A, B]

Terminate = False

while not Terminate:
    if listy[-2] - listy[-1] <= listy[-1]:
        listy.append(listy[-2]-listy[-1])
    else:
        Terminate = True
print (len(listy)+1)