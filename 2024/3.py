import heapq
import re
from collections import Counter

input_list = []

with open("2.txt", encoding='utf-8') as file:
    for line in file:
        input_list.append(line)
    input_string = "".join(map(str,input_list))
    print(input_string)


mapping = {
        'm': 'u',
        'u': 'l',
        'l': '(',
        '(': ',',
        ',': ')'
        }

to_sum = []

def check_valid(input_string, index):
    index += 1
    number1 = []
    number2 = []
    initial = index-1

    while index < len(input_string):
        if input_string[index-1] not in mapping:
            return index

        if input_string[index] == mapping[input_string[index-1]] and input_string[index]!= '(':
            index += 1
            continue
        else:
            if input_string[index] != mapping[input_string[index-1]]:
                return index
            index += 1
            while index < len(input_string) and input_string[index] != ',' and len(number1) < 3:
                if not input_string[index].isdigit():
                    return index
                else:
                    number1.append(input_string[index])
                index += 1

            if index >= len(input_string) or input_string[index] != ',':
                return index
            else:
                index += 1

                while index < len(input_string) and input_string[index] != ')' and len(number2) < 3:
                    if not input_string[index].isdigit():
                        return index 
                    else:
                        number2.append(input_string[index])
                    index += 1
                if index >= len(input_string) or input_string[index] != ')':
                    return index
                else:
                    index += 1
                    break

    if number1 and number2: 
        n1 = int("".join(map(str,number1))) 
        n2 = int("".join(map(str,number2)))
        string1 = "mul("+str(n1)+"," + str(n2) + ")"
        to_sum.append(n1*n2)
    return index

def check_permission(input_string, index):

    if index + 7 <= len(input_string):
        if input_string[index:index+7] == 'don\'t()':
            return 7
        elif input_string[index:index+4] == 'do()':
            return 4
    return 1

def do_multiplication(input_string):

    permission = 1
    i = 0
    while i < len(input_string):
        if input_string[i] != 'm' and input_string[i] != 'd':
            i+=1
            continue
        elif input_string[i] == 'd':
            perm = check_permission(input_string,i)
            i+=perm
            if perm != 1:
                permission = perm
        else:
            if permission == 7:
                i+=1
                continue
            i = check_valid(input_string,i)

    return sum(to_sum)


print(do_multiplication(input_string))
