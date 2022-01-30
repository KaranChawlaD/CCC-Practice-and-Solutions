briefcase_value = {
    "1":100,
    "2":500,
    "3":1000,
    "4":5000,
    "5":10000,
    "6":25000,
    "7":50000,
    "8":100000,
    "9":500000,
    "10":1000000,
    }
n = int(input())
briefcase_chosen = []
for i in range(n):
    briefcase_chosen.append(str(input()))

TotalSum = 1691600
for i in range (len(briefcase_chosen)):
    TotalSum = TotalSum - briefcase_value[str(briefcase_chosen[i])]

Average = TotalSum / (10-n)

if (Average>int(input())):
    print ("no deal")
else:
    print ("deal")