import heapq
from collections import Counter

input_list = []

with open("6.txt", encoding='utf-8') as file:
    for line in file:
        cleared_line = line[:len(line)-1] if line[-1] == '\n' else line
        input_list.append(cleared_line)

operations = input_list[-1].split()
number_list = []

for i in range(0,len(input_list)-1):
    str_list = input_list[i].split()
    number_list.append([int(n) for n in str_list])
    


def do_operation(number_list, operations):

    map = {
        '+': lambda x,y: x+y,
        '*': lambda x,y: x*y
    }
    
    result_list = []
    
    for op in operations:
        if op == '+':
            result_list.append(0)
        else:
            result_list.append(1)
    
    for row in number_list:
        for i, n in enumerate(row):
            result_list[i] = map[operations[i]](result_list[i],n)
            
        
    return sum(result_list)


print(do_operation(number_list,operations))
