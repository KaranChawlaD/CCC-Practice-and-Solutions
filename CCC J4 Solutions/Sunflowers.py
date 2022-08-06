N = int(input())

arr = []

for l in range(N):
    temp = [int(x) for x in input().split()]
    arr.append(temp)

def rotate(array):
    temp_array = []
    temp = []
    for s in range(N):
        for r in range(N):
            temp.append(0)
        temp_array.append(temp)
        temp = [] 
    for q in range(N):
        for p in range(N):
            temp_array[N-p-1][q] = array[q][p]
    return temp_array

def check(array):
    for q in range(N):
        for p in range(N-1):
            if array[q][p] > array[q][p+1]:
                return False
    for q in range(N-1):
        if array[q][0] > array[q+1][0]:
            return False
    else:
        return True

def output(array):
    for_printing = []
    for q in range(N):
        output = ''
        for p in range(N):
            output = output + str(array[q][p]) + ' '
        for_printing.append(output)
    for e in range(len(for_printing)):
        print(for_printing[e])

if check(arr):
    output(arr)
else:
    arr = rotate(arr)
    if check(arr):
        output(arr)
    else:
        arr = rotate(arr)
        if check(arr):
            output(arr)
        else:
            arr = rotate(arr)
            if check(arr):
                output(arr)