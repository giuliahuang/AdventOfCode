import heapq
from collections import Counter

input_list = []

with open("2.txt", encoding='utf-8') as file:
    for line in file:
        input_list.append(line)

input_string = "".join(map(str,input_list))

interval_strings = input_string.split(",")

intervals = []

for inter in interval_strings:
    elem = inter.split('-')
    intervals.append(elem)

print(intervals)

def find_invalid_IDs(intervals):

    res = 0
    
    for start, end in intervals:
    
        start = str(int(start))
        end = str(int(end))
        
        s_digits = len(start)
        e_digits = len(end)
        
        # ensuring 2 divisible
        if s_digits % 2 != 0:
            s_digits += 1
            start = "1" + "0" * (s_digits-1)
        
        if e_digits % 2 != 0:
            e_digits -= 1
            end = "9" * e_digits
        
        if s_digits > e_digits or int(start) > int(end):
            continue
        
        # adjust intervals:
        if int(start[len(start)//2:]) > int(start[:len(start)//2]):
            start_count = int(start[:len(start)//2]) + 1
        else:
            start_count = int(start[:len(start)//2])
            
        if int(end[len(end)//2:]) >= int(end[:len(end)//2]):
            end_count = int(end[:len(end)//2])
        else:
            end_count = int(end[:len(end)//2]) - 1
            
        if start_count > end_count:
            continue
            
        for i in range(start_count,end_count+1):
            res += int(str(i) * 2)
    
        
    return res

print(find_invalid_IDs(intervals))
