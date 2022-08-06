Stop = False

while not Stop:
    Input = input().split()
    Check = 0
    Input_Check = 1
    Cycle = []

    if Input[0] == "0":
        Stop = True
    else:
        for i in range(len(Input)):
            Input[i] = int(Input[i])
        Input.pop(0)
        if len(Input) > 1:
            Cycle.append(Input[1] - Input[0])
            for k in range(2, len(Input)):
                if ((Input[k] - Input[k-1]) == Cycle[Check]):
                    Check += 1
                    if Check == len(Cycle):
                        Check = 0
                else:
                    for l in range(Input_Check, k):
                        Cycle.append(Input[l+1] - Input[l])
                    Input_Check = k
                    Check = 0

        print (len(Cycle))