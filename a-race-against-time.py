#!/bin/python3

# Complexity O(N^2)

import sys

def raceAgainstTime(n, mason_height, heights, prices):
    ch = mason_height
    heights = [mason_height] + heights
    prices = [0] + prices
    
    # Finding next higher height
    next_max = [0]*n
    for i in range(n):
        ii=i+1
        while ii<n and heights[i]>=heights[ii]:
            ii += 1
        
        if ii<n:
            next_max[i] = ii
        else:
            next_max[i] = -1
                                           
    
    res = [0]*n
    for i in range(n-1, -1, -1):
        if next_max[i] == -1:
            min_res = n-i
            ii = n
        else:
            ii = next_max[i]
            min_res = (ii-i) + abs(heights[i]-heights[ii]) + prices[ii] + res[ii]
        for j in range(i+1, ii):
            if min_res > res[j] + abs(heights[i]-heights[j]) + prices[j] + (j-i):
                min_res = res[j] + abs(heights[i]-heights[j]) + prices[j] + (j-i)
        res[i] = min_res

    return res[0]    

if __name__ == "__main__":
    n = int(input().strip())
    mason_height = int(input().strip())
    heights = list(map(int, input().strip().split(' ')))
    prices = list(map(int, input().strip().split(' ')))
    result = raceAgainstTime(n, mason_height, heights, prices)
    print(result)
