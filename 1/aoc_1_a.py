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

xList.sort()
yList.sort()
# print(xList)
# print(yList)
for i in range(len(xList)):
    sum += abs(xList[i] - yList[i])

print(sum)