import re

with open('AOC/3/input.csv', 'r') as file:
    fileContent = file.read().replace("\n", "")
pattern = r"mul\(\d+,\d+\)"

matches = re.findall(pattern, fileContent)
sum = 0
for i in matches:
    num_p = r"\d+"
    list_p = re.findall(num_p, i)
    sum += int(list_p[0]) * int(list_p[1])
    
print(sum)