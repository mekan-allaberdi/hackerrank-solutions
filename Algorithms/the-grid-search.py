#!/bin/python3

import sys

def gridSearch(M, P, n, m, pn, pm):
    for i in range(n-pn+1):
        for j in range(m-pm+1):
            matching = False
            for ii in range(pn):
                for jj in range(pm):
                    matching = M[i+ii][j+jj] == P[ii][jj]
                    if not matching:
                        break
                if not matching:
                        break
            if matching:
                return 'YES'
    return 'NO'
                        

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n, m = map(int, input().strip().split(' '))
        matrix = []
        for _ in range(n):
            i_list = list(input())
            matrix.append(i_list)
        pn, pm = map(int, input().strip().split(' '))
        pattern = []
        for _ in range(pn):
            i_list = list(input())
            pattern.append(i_list)
        result = gridSearch(matrix, pattern, n, m, pn, pm)
        print(result)
