from tabnanny import check


board = [[1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8]]

knight_coordinates = input().split()
knight_start_x = int(knight_coordinates[0])
knight_start_y = int(knight_coordinates[1])

target_coordinates = input().split()
target_x = int(target_coordinates[0])
target_y = int(target_coordinates[1])

checked_x = [knight_start_x]
checked_y = [knight_start_y]

Found = False
Check = False
Zero = False
Old_Length = 0

Moves = 1

def target_check(x_coordinate, y_coordinate):
    if abs(target_x - x_coordinate) == 2 and abs(target_y - y_coordinate) == 1:
        return True
    elif abs(target_y - y_coordinate) == 2 and abs(target_x - x_coordinate) == 1:
        return True
    else:
        return False

if knight_start_x == target_x and knight_start_y == target_y:
    print ("0")
    Found = True
    Zero = True

while not Found:
    for i in range(len(checked_x)):
        Check = target_check(checked_x[i], checked_y[i])
        if Check:
            Found = True

    if not Found:
        Old_Length = len(checked_x)
        for k in range(len(checked_x)):
            if checked_x[k] + 2 <= 8 and checked_y[k] + 1 <= 8:
                checked_x.append(checked_x[k] + 2)
                checked_y.append(checked_y[k] + 1)
            if checked_x[k] - 2 >= 1 and checked_y[k] + 1 <= 8:
                checked_x.append(checked_x[k] - 2)
                checked_y.append(checked_y[k] + 1)         
            if checked_x[k] + 2 <= 8 and checked_y[k] - 1 >= 1:
                checked_x.append(checked_x[k] + 2)
                checked_y.append(checked_y[k] - 1)
            if checked_x[k] - 2 >= 1 and checked_y[k] -1 >= 1:
                checked_x.append(checked_x[k] - 2)
                checked_y.append(checked_y[k] - 1) 
            if checked_x[k] + 1 <= 8 and checked_y[k] + 2 <= 8:
                checked_x.append(checked_x[k] + 1)
                checked_y.append(checked_y[k] + 2)
            if checked_x[k] - 1 >= 1 and checked_y[k] + 2 <= 8:
                checked_x.append(checked_x[k] - 1)
                checked_y.append(checked_y[k] + 2)
            if checked_x[k] + 1 <= 8 and checked_y[k] - 2 >= 1:
                checked_x.append(checked_x[k] + 1)
                checked_y.append(checked_y[k] - 2)
            if checked_x[k] - 1 >= 1 and checked_y[k] - 2 >= 1:
                checked_x.append(checked_x[k] - 1)
                checked_y.append(checked_y[k] - 2)
        for m in range(Old_Length):
            checked_x.pop(0)
            checked_y.pop(0)
        Moves += 1

if not Zero:
    print (Moves)