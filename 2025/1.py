import heapq
from collections import Counter

input_list = []

with open("1.txt", encoding='utf-8') as file:
    for line in file:
        input_list.append(line)



def count_zero(input_list):
    count = 50
    res = 0
    for i in input_list:
        direction = i[0]
        number = int(i[1:])

        if direction == 'R':
            count = (count+number)
        elif direction == 'L':
            prev = count
            count = (count-number)
            if number > prev and prev!= 0:
                res += 1

        if count == 0:
            res += 1

        res = res + (abs(count)//100)
        count = count%100

    return res

print(count_zero(input_list))
