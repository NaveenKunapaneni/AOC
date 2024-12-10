from collections import Counter

def check_dec_order(x):
    for i in range(1,len(x)):

        diff = x[i-1] - x[i]
        if x[i-1] <= x[i]:
            return False
        elif 1 < diff > 3:
            return False
        
    return True

def check_asc_order(x):
    for i in range(1,len(x)):
        diff = x[i] - x[i-1]
        if x[i-1] >= x[i]:
            return False
        elif 1 < diff > 3:
            return False
        
    return True
    
def check_dec_order_aftr_rmvl(x):
    for i in range(len(x)):
        temp = x[:i] + x[i+1:]
        # valid = True
        for j in range(1,len(temp)):
            # if temp[j-1] <= temp[j]:
            #     valid = False
            #     break
            # elif abs(temp[j-1] - temp[j]) > 3:
            #     valid = False
            #     break
            if check_dec_order(temp):
                return True
            
        # if valid:
        #     return True
    return False
    
def check_asc_order_aftr_rmvl(x):
    for i in range(len(x)):
        temp = x[:i] + x[i+1:]
        # valid = True
        for j in range(1,len(temp)):
            # if temp[j-1] >= temp[j]:
            #     valid = False
            #     break
            # elif 1 <= abs(temp[j] - temp[j-1]) >= 3:
            #     valid = False
            #     break
            if check_asc_order(temp):
                return True
            
        # if valid:
        #     return True
    return False


xList = []
count1 = 0
count2 = 0

with open('AOC/2/input.csv', 'r') as file:
    for line in file:
        if not line:
            break
        line.strip()

        x = list(map(int, line.split()))
        # print([check_asc_order(x), check_dec_order(x), check_asc_order_aftr_rmvl(x), check_dec_order_aftr_rmvl(x)])
        if check_asc_order(x) or check_dec_order(x):
            # print("Safe")
            count1 += 1
        if check_asc_order_aftr_rmvl(x) or check_dec_order_aftr_rmvl(x):
            count2 += 1
            # print("Safe")
        # else:
        #     print("UnSafe")

print(count1, count2)