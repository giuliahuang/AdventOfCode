import heapq
from collections import Counter

input_list = []

with open("3.txt", encoding='utf-8') as file:
    for line in file:
        input_list.append(str(int(line)))

#print(input_list)


def find_largest(bank, n_bat):

    if len(bank) <= n_bat:
        return int(bank) if len(bank) != 0 else 0
    
    batteries = [-1 for i in range(n_bat)]
    indices = [-1 for i in range(n_bat)]
    
    batteries[0] = int(bank[0])
    indices[0] = 0
    
    last_index = -1
    
    i = 1
    
    while i < len(bank):
        for j in range(len(batteries)):
            # if the new number is greater or its value became invalid
            if int(bank[i]) > batteries[j] or (indices[j] < indices[last_index] and last_index < j):
                if i + n_bat-j-1 < len(bank):
                    indices[j] = i
                    batteries[j] = int(bank[i])
                    last_index = j
                    break

        i+=1
    
    result = 0

    for i, b in enumerate(batteries):
        result += b * 10**(len(batteries)-1-i)

    return result
        
    
                


def sum_largest(input_list):

    res = 0

    for bank in input_list:
        res += find_largest(bank, 12)
    
    return res
    

print(sum_largest(input_list))
