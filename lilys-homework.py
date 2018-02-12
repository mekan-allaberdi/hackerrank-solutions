# Python3
# Sorting and using Map

#!/bin/python3

import sys
import copy

def lilysHomework(arr, n, reversed):
    swap_count = 0
    sorted = copy.deepcopy(arr)
    sorted.sort(reverse=reversed)
    mp = {}
    for i in range(n):
        mp[arr[i]] = i
    
    for i in range(n):
        curr_num = arr[i]
        sorted_num = sorted[i]
        if curr_num != sorted_num:
            swap_count += 1
            sorted_ind = mp[sorted_num]
            arr[i], arr[sorted_ind] = arr[sorted_ind], arr[i]
            mp[curr_num] = mp[sorted_num]
            
    return swap_count
            

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    arr2 = copy.deepcopy(arr)
    result = min(lilysHomework(arr, n, False),lilysHomework(arr2, n, True))
    print(result)
