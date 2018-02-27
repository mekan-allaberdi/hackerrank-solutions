#!/bin/python3

import sys
import copy

max_num = 10**20
min_loss = max_num

def merge(left, right):
    global min_loss
    arr = []
    n = len(left) + len(right)
    left.append(max_num)
    right.append(max_num)
    for k in range(n):
        if left[0] < right[0]:
            arr.append(left[0])
            left.remove(left[0])
        else:
            arr.append(right[0])
            min_loss = min(min_loss, left[0]-right[0])
            right.remove(right[0])
    return arr

def div_and_conq(price):
    if len(price) < 2:
        return price
    q = len(price)//2
    left = div_and_conq(price[:q])
    right = div_and_conq(price[q:])
    return merge(left, right)
    

def minimumLoss(price):
    n = len(price)
    div_and_conq(price)

if __name__ == "__main__":
    n = int(input().strip())
    price = list(map(int, input().strip().split(' ')))
    minimumLoss(price)
    print(min_loss)
