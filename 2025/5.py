import heapq
from collections import Counter

ranges = []
ids = []

with open("5.txt", encoding='utf-8') as file:

    jump = False
    for line in file:
        if line == '\n':
            jump = True
            continue
                
        cleared_line = line[:len(line)-1] if line[-1] == '\n' else line
        ranges.append(cleared_line) if not jump else ids.append(cleared_line)

intervals = [r.split('-') for r in ranges]
ids = [int(id) for id in ids]
ids = sorted(ids)

print("intervals:", intervals)
print("ids:", ids)


def check_within_intervals(ids, intervals):

    n_fresh_ing = 0


    intervals = sorted(intervals, key = lambda x: int(x[0]))
    no_overlap_int = []
    s_start, s_end = int(intervals[0][0]),int(intervals[0][1])
    
    for i in range(1, len(intervals)):
        start, end = int(intervals[i][0]), int(intervals[i][1])
        
        if start <= s_end:
            s_end = max(end,s_end)
        else:
            n_fresh_ing += (s_end - s_start + 1)
            no_overlap_int.append([s_start, s_end])
            s_start, s_end = start, end
    
    count = 0
    
    no_overlap_int.append([s_start, s_end])
    n_fresh_ing += (s_end - s_start + 1)
    
    interval_index = 0
    
    for id in ids:
    
        start, end = no_overlap_int[interval_index]
        if id < start:
            print(f"{id} NOT in range({start},{end})")
            continue
        
        if id > end:
            while interval_index < len(no_overlap_int):
                start, end = no_overlap_int[interval_index]
                print(f"CHECKING {id} in range({start},{end})?")
                if id > end:
                    interval_index+=1
                else:
                    break
            
            if interval_index >= len(no_overlap_int):
                print("index reached")
                break
            
        if id in range(start,end+1):
            print(f"{id} in range({start},{end})")
            count+=1
        else:
            print(f"{id} NOT in range({start},{end})")
            
    print("N_fresh_ing: ", n_fresh_ing)
    return count
    

print(check_within_intervals(ids,intervals))
    


