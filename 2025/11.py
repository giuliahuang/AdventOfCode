import heapq
import collections
from collections import Counter
import re

input_list = []

with open("10.txt", encoding='utf-8') as file:
    indicators = []
    buttons = []
    joltages = []
    for line in file:

        def parse_line(line):
            # 1) First element: [.##.]
            first_match = re.search(r'\[([.#]+)\]', line)
            first_array = list(first_match.group(1))

            # 2) Second elements: (3) (1,3) (2) ...
            second_matches = re.findall(r'\(([^)]+)\)', line)
            second_array = [
                list(map(int, item.split(',')))
                for item in second_matches
            ]

            # 3) Third element: {3,5,4,7}
            third_match = re.search(r'\{([^}]+)\}', line)
            third_array = list(map(int, third_match.group(1).split(',')))

            return first_array, second_array, third_array

        first, second, third = parse_line(line)
        indicators.append(first)
        buttons.append(second)
        joltages.append(third)


print('indicators', indicators)
print('buttons', buttons)
print('joltages', joltages)


def find_comb(indicators, buttons):

    mapping = {
        '.': '#',
        '#': '.'
    }

    def dfs(i, button, indicator, array):

        if array == indicator:
            return 0
        if i >= len(button):
            return float("inf")
        
        # check if equal
        yes, no = array.copy(), array.copy() 

        res = dfs(i+1, button, indicator, no)
        for b in button[i]:
            switch = yes[b]
            yes[b] = mapping[switch]

        res = min(res, 1+dfs(i+1,button, indicator,yes))

        return res
    
    count = 0

    for button, indicator in zip(buttons, indicators):
        
        initial = ['.' for i in range(len(indicator))]
        res = dfs(0, button, indicator, initial)
        count += res


    return count

# def find_jolt(joltages, buttons):

#     def dfs(i, button, joltage, array, memo):
#         state = (i, tuple(array))
#         if state in memo:
#             return memo[state]

#         if array == joltage:
#             return 0
        
#         if i >= len(button):
#             return float("inf")
        
#         # check if equal
#         yes, no = array.copy(), array.copy() 

#         res = dfs(i+1, button, joltage, no, memo)
#         for b in button[i]:
#             yes[b] += 1
#             if yes[b] > joltage[b]:
#                 memo[state] = res
#                 return res

#         res = min(res, 1+dfs(i,button, joltage, yes, memo))
#         memo[state] = res

#         return res
    
#     count = 0

#     for button, joltage in zip(buttons, joltages):
#         memo = {} 
#         initial = [0 for i in range(len(joltage))]
#         res = dfs(0, button, joltage, initial, memo)
#         print(res)
#         count += res

#     return count

from collections import deque

def min_presses(button, joltage):
    m = len(joltage)
    start = tuple(0 for _ in range(m))
    target = tuple(joltage)

    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        state, cost = queue.popleft()

        if state == target:
            return cost

        for btn in button:
            new_state = list(state)
            valid = True
            for b in btn:
                new_state[b] += 1
                if new_state[b] > joltage[b]:
                    valid = False
                    break

            if not valid:
                continue

            new_state = tuple(new_state)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, cost + 1))

    return float("inf")

def find_jolt(joltages, buttons):
    total = 0
    for button, joltage in zip(buttons, joltages):
        res = min_presses(button, joltage)
        print(res)
        total += res
    return total


print(find_comb(indicators, buttons))
print(find_jolt(joltages, buttons))