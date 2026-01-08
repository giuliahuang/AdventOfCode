import heapq
from collections import Counter
a1 = []
a2 = []

with open("1.txt", encoding='utf-8') as file:
    for line in file:
        elements = line.split()

        a1.append(int(elements[0]))
        a2.append(int(elements[1]))

def compare_min(a1, a2):
    list1 = a1.copy()
    list2 = a2.copy()
    heapq.heapify(list1)
    heapq.heapify(list2)
    dis = 0

    for _ in range(0, len(a1)):
        dis+= abs(heapq.heappop(list1) - heapq.heappop(list2))
    
    return dis

def count_on_right_list(a1,a2):
    counter2 = Counter(a2)
    total = 0
    
    for elem in a1:
        if elem in counter2:
            total += counter2[elem] * elem

    return total

print(compare_min(a1,a2))
print(count_on_right_list(a1,a2))
