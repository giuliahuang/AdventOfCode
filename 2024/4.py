import heapq
import re
from collections import Counter

input_list = []

with open("4.txt", encoding='utf-8') as file:
    for line in file:
        input_list.append(line)
        
def is_valid(r,c,dr,dc,input_list):
    if min(r,c) < 0 or min(r+dr,c+dc) < 0 or r >= ROWS or c >= COLS or r+dr >= ROWS or c+dc >= COLS:
        return False
    return True
        
def dfs(r,c, dr, dc, input_list, word, i):

    if i >= len(word):
        return True
        
    if not is_valid(r,c,dr,dc,input_list):
        return False
    
    nr = r+dr
    nc = c+dc
    
    if input_list[nr][nc] != word[i]:
        return False
    
    return dfs(nr,nc,dr,dc,input_list, word, i+1)
    

        
    
ROWS = len(input_list)
COLS = len(input_list[0])



def find_word(input_list):

    directions = [[0,1],[0,-1],[1,0],[-1,0],[-1,-1],[-1,1],[1,-1],[1,1]]
    count = 0
    
    for r in range(ROWS):
        for c in range(COLS):
            if input_list[r][c] == 'X':
                for dr, dc in directions:
                    if dfs(r,c,dr,dc, input_list, 'MAS', 0):
                        count += 1
    
    return count
    
    


def dfs_2(r,c, dr, dc, input_list, word, i, check_matrix):
        
    if not is_valid(r,c,dr,dc,input_list):
        return 0
    
    nr = r+dr
    nc = c+dc
    
    if input_list[nr][nc] != word[i]:
        return 0
    
    if i == len(word) -1:
        check_matrix[r][c] += 1
        if check_matrix[r][c] == 2:
            return 1
        return 0
        
    
    return dfs_2(nr,nc,dr,dc,input_list,word,i+1,check_matrix)
    
    
def find_X(input_list):
    
    directions = [[-1,-1],[-1,1],[1,-1],[1,1]]
    check_matrix = [[0 for i in range(ROWS)] for j in range(COLS)]
    count = 0
    
    for r in range(ROWS):
        for c in range(COLS):
            if input_list[r][c] == 'M':
                for dr, dc in directions:
                    count += dfs_2(r,c,dr,dc, input_list, 'AS', 0, check_matrix)
            
    return count
    
print(find_word(input_list))

print(find_X(input_list))
    
    
    
