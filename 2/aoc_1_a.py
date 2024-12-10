from collections import Counter

def check_dec_order(x):
    for i in range(1,len(x)):
        if x[i-1] <= x[i]:
            return False
        elif x[i-1] - x[i] > 3:
            return False
        
    return True

def check_asc_order(x):
    for i in range(1,len(x)):
        if x[i-1] >= x[i]:
            return False
        elif x[i] - x[i-1] > 3:
            return False
        
    return True

xList = []
count = 0

with open('AOC/2/input.csv', 'r') as file:
    for line in file:
        if not line:
            break
        line.strip()

        x = list(map(int, line.split()))
        if check_asc_order(x) or check_dec_order(x):
            print("Safe")
            count += 1
        else:
            print("unsafe")

print(count)