# python3

def ransom_note(magazine, ransom):
    d = dict()
    for w in magazine:
        count = d.get(w, 0)
        d[w] = count + 1
    
    for w in ransom:
        count = d.get(w, 0)
        if count == 0:
            return False
        d[w] = count-1
    
    return True
        

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    
