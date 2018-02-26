cube = lambda x: x**3 

def fibonacci(n):
    flist = [0, 1] 
    for i in range(2,n):
        flist.append(flist[i-1] + flist[i-2])
    return flist[:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
