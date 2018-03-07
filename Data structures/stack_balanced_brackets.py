closing_pairs = {')': '(', ']': '[', '}': '{'}

def is_matched(expression):
    my_stack = []
    for p in expression:
        if closing_pairs.get(p, False):
            if len(my_stack) == 0:
                return False
            last_p = my_stack.pop()
            open_p = closing_pairs[p]
            if last_p != open_p:
                return False
        else:
            my_stack.append(p)
    
    return len(my_stack)==0
            

t = int(input().strip())
for _ in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
