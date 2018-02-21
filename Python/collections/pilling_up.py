# python3

from collections import deque

def check_cubes(arr, n):
    d = deque(arr)
    
    last_cube = 2**31 
    for i in range(n-1, -1, -1):
        left = d[0]
        right = d[i]
        
        new_cube = max(left, right)
        if new_cube > last_cube:  # if max of left and right less than last stacked cube, it is not possible
            print('No')
            return
        
        last_cube = new_cube
        if left > right:
            d.popleft()
        else:
            d.pop()
     
    print('Yes')
        

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        check_cubes(arr, n)
