A = 0
B = 0

Seven = False

Output = []

while Seven == False:
    Input = input().split(" ")

    if int(Input[0]) == 1:
        if Input[1] == "A":
            A = int(Input[2])
        else:
            B = int(Input[2])

    elif int(Input[0]) == 2:
        if Input[1] == "A":
            Output.append(A)
        else:
            Output.append(B)

    elif int(Input[0]) == 3:
        if Input[1] == "A":
            if Input[2] == "B":
                A = A + B
            else:
                A = A + A
        elif Input[2] == "B":
            B = B + B
        else:
            B = B + A

    elif int(Input[0]) == 4:
        if Input[1] == "A":
            if Input[2] == "B":
                A = A * B
            else: 
                A = A * A
        elif Input[2] == "A":
            B = A * B
        else:
            B = B * B

    elif int(Input[0]) == 5:
        if Input[1] == "A":
            if Input[2] == "B":
                A = A - B
            else:
                A = A - A
        elif Input[2] == "A":
            B = B - A
        else:
            B = B - B

    elif int(Input[0]) == 6:
        if Input[1] == "A":
            if Input[2] == "B":
                A = A//B
            else:
                A = A//A
        elif Input[2] == "A":
            B = B//A
        else:
            B = B//B
    else:
        Seven = True

for i in range(len(Output)):
    print (Output[i])