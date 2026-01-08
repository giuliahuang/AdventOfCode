import heapq
from collections import Counter

input_list = []

with open("2.txt", encoding='utf-8') as file:
    for line in file:
        elements = line.split()
        input_list.append([int(e) for e in elements])

print(input_list)

def check_two_numbers(comparison, n1, n2):
    if comparison == 1:
        if n1 - n2 > 3 or n1 - n2 < 1:
            return False
    elif comparison == 0:
        if n2 - n1 > 3 or n2 - n1 < 1:
            return False
    return True

def check_line(line):

    comparison = -1

    for i in range(1, len(line)):
        if (line[i-1] - line[i]) == 0:
            return False
    
        if comparison == -1:
            if(line[i-1] - line[i]) > 0:
                comparison = 1
            else:
                comparison = 0
        
        if not check_two_numbers(comparison, line[i-1], line[i]):
            return False
    return True



def check_reports(input_list):
    count_safe = 0

    for line in input_list:

        safe = 0

        if not check_line(line):
            for i in range(0, len(line)):
                if check_line(line[:i] + line[i+1:]):
                    safe = 1
                    break
        else:
            safe = 1

        count_safe += safe
        
    return count_safe

print(check_reports(input_list))






