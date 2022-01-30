letter_location_x = {
    "A":0,
    "B":1,
    "C":2,
    "D":3,
    "E":4,
    "F":5,   
    "G":0,
    "H":1,
    "I":2,
    "J":3,
    "K":4,
    "L":5,
    "M":0,
    "N":1,
    "O":2,
    "P":3,
    "Q":4,
    "R":5,   
    "S":0,
    "T":1,
    "U":2,
    "V":3,
    "W":4,
    "X":5,   
    "Y":0,
    "Z":1,
    " ":2,
    "-":3,
    ".":4,
    "enter":5,
    }
letter_location_y = {
    "A":0,
    "B":0,
    "C":0,
    "D":0,
    "E":0,
    "F":0,   
    "G":1,
    "H":1,
    "I":1,
    "J":1,
    "K":1,
    "L":1,
    "M":2,
    "N":2,
    "O":2,
    "P":2,
    "Q":2,
    "R":2,   
    "S":3,
    "T":3,
    "U":3,
    "V":3,
    "W":3,
    "X":3,   
    "Y":4,
    "Z":4,
    " ":4,
    "-":4,
    ".":4,
    "enter":4,
    }
n = str(input())
listy = list(n)

currentX = 0
currentY = 0
neededX = 0
neededY = 0
moves = 0
for i in range (len(listy)):
    neededX = letter_location_x[listy[i]]
    neededY = letter_location_y[listy[i]]
    moves = moves + (abs(neededX-currentX)) + (abs(neededY - currentY))
    currentX = neededX
    currentY = neededY

moves = moves + (5-currentX) + (4-currentY)
print (moves)