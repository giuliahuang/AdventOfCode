import heapq
import collections
from collections import Counter

input_list = []

with open("8test.txt", encoding='utf-8') as file:
    for line in file:
        cleared_line = line[:len(line)-1] if line[-1] == '\n' else line
        input_list.append([int(n) for n in cleared_line.split(',') ])

def compute_distance(p1, p2):

    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2
    

print(input_list)

class Node:
    def __init__(self, value):
        self.element = value
        self.next = None

    def getElement(self):
        return self.element
    
    def getNext(self):
        return self.next

def compute_circuits(input_list):
    
    closest_graph = {}

    for i, p1 in enumerate(input_list):
        dist = float("inf")
        for j, p2 in enumerate(input_list):
            if i == j:
                continue
            new_dist = compute_distance(p1,p2)
            if new_dist < dist:
                closest_graph[i] = j
                dist = new_dist
        
        print(f"{p1} is closest to {input_list[ closest_graph[i] ]} with dist: {dist}")
        
    connected_graph = collections.defaultdict(list)
    for k, v in closest_graph.items():
        if v not in connected_graph[k]:
            connected_graph[k].append(v)
        if k not in connected_graph[v]:
            connected_graph[v].append(k)

    print("closest_graph", closest_graph)
    print("connected_graph", connected_graph)

    global_visited = set()

    def dfs(i, visited):
        if i in visited:
            return 
        
        visited.add(i)
        dfs(closest_graph[i], visited)
        

    count = 1
    
    for k, v in connected_graph.items():
        visited = set()
        if k not in global_visited:
            print(k)
            dfs(k,visited)

            print("visited: ", visited)
            count *= len(visited)
            global_visited.update(visited)
    
    return count

print( compute_circuits(input_list) )
