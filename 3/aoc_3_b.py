import re

with open('AOC/3/input.csv', 'r') as file:
    fileContent = file.read().replace("\n", "")
pattern = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"
matches = re.findall(pattern, fileContent)

print(matches)
sum = 0
enable = True

for i in matches:
    if i.startswith("don't"):
        enable = False
    elif i.startswith("do"):
        enable = True
    elif i.startswith("mul(") and enable:
        num_p = r"\d+"
        list_p = re.findall(num_p, i)
        sum += int(list_p[0]) * int(list_p[1])
    
print(sum)