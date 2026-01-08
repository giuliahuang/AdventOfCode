import heapq
from collections import Counter

input_list = []

with open("7.txt", encoding='utf-8') as file:
    for line in file:
        cleared_line = line[:len(line)-1] if line[-1] == '\n' else line
        input_list.append(cleared_line)

def splitter(input_list):
    
    ROWS = len(input_list)
    COLS = len(input_list[0])
    
    map = [0 if input_list[0][i]!='S' else 1 for i in range(COLS)]
    
    
    count = 0
    
    n_ways = 0
    
    for r in range(1, ROWS):
        if r % 2 != 0:
            continue
        for index in range(COLS):
            if input_list[r][index] == '^':
                if map[index] == 1:
                    count += 1
                    map[index] = 0
                    if index - 1 >= 0 and index - 1 < COLS:
                        map[index-1] = 1
                    if index + 1 < COLS:
                        map[index+1] = 1
        print(map)
        n_ways+=sum(map)
            
    return count, n_ways
            
            

    
    
print(splitter(input_list))
