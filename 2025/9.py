import heapq
import collections
from collections import Counter

input_list = []

with open("9.txt", encoding='utf-8') as file:
    for line in file:
        cleared_line = line[:len(line)-1] if line[-1] == '\n' else line
        input_list.append([int(n) for n in cleared_line.split(',') ])

def compute_distance(p1, p2):

    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 
    


def compute_circuits(input_list):
    
    max_area = 0

    for i, p1 in enumerate(input_list):
        dist = 0 
        for j, p2 in enumerate(input_list):
            if i == j:
                continue
            new_dist = compute_distance(p1,p2)
            if new_dist > dist:
                area = (abs(p1[0]-p2[0])+1) * (abs(p1[1]-p2[1])+1)
                max_area = max(max_area, area)
                dist = new_dist
    
    return max_area 

print( compute_circuits(input_list) )
