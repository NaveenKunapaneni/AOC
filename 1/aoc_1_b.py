from collections import Counter

xList = []
yList = []
sum = 0

with open('AOC/1/input.csv', 'r') as file:
    for line in file:
        if not line:
            break
        line.strip()

        x,y = map(int, line.split())
        xList.append(x)
        yList.append(y)

cnt2 = Counter(yList)

sum2prod = 0
for i in xList:
    if i in cnt2:
        prod = cnt2[i] * i
        sum2prod += prod
    
print(sum2prod)