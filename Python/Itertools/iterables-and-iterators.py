# pythpon3

from itertools import combinations

def find_a_comb(letters, k):
    combs = list(combinations(letters, k))
    res = 0
    for c in combs:
        res += 'a' in c

    return res/len(combs)

if __name__ == '__main__':
    n = int(input())
    letters = list(input().split())
    k = int(input())
    
    occ_a = find_a_comb(letters, k)
    print(occ_a)

