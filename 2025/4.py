import heapq
from collections import Counter

input_list = []

with open("4.txt", encoding='utf-8') as file:
    for line in file:
        input_list.append(line[:len(line)-1])

print(input_list)

ROWS = len(input_list)
COLS = len(input_list[0])

def is_valid(r,c):
    if min(r,c) < 0 or r>= ROWS or c>=COLS:
        return False
    if input_list[r][c] != '@':
        return False
    return True

def check_access(input_list):

    
    directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
    
    check_matrix = [[0 for i in range(ROWS)] for j in range(COLS)]

    for r in range(ROWS):
        for c in range(COLS):
            if input_list[r][c] == '@':
                for dr, dc in directions:
                    nr = r+dr
                    nc = c+dc
                    if is_valid(nr,nc):
                        check_matrix[nr][nc] += 1
            else:
                check_matrix[r][c] = -1
    
    total_count = 0
    
    def deep_copy(A):
        return [r[:] for r in A]
    
            

    while True:
        count = 0
        
        matrix_tmp = deep_copy(check_matrix)
        print(matrix_tmp)
    
        for r in range(ROWS):
            for c in range(COLS):
                if check_matrix[r][c] < 4 and check_matrix[r][c] >= 0:
                    for dr, dc in directions:
                        nr = r+dr
                        nc = c+dc
                        if is_valid(nr,nc):
                            matrix_tmp[nr][nc] -= 1
                    matrix_tmp[r][c] = -1
                    count += 1
        
        check_matrix = deep_copy(matrix_tmp)
        
        if count == 0:
            break
                    
        total_count += count

        
                
    return total_count
    
print(check_access(input_list))
            
                    
            
        
        
