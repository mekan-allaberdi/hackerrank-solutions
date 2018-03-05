# python3
'''
  Problem : 
  Given the words in the magazine and the words in the ransom note, 
  print Yes if he can replicate his ransom note exactly using whole words from the magazine; 
  otherwise, print No.

  input :
    <n>: number of words in the magazine, <m>: number of words in the ransom note
    <magazine_words>
    <ransome note words>
    
  output:
    Print Yes if he can use the magazine to create an untraceable replica of his ransom note; otherwise, print No.
  
  Sample Input 0
  6 4
  give me one grand today night
  give one grand today 
  
  Sample Output 0
  Yes

  Sample Input 1
  6 5
  two times three is not four
  two times two is four
  
  Sample Output 1
  No
'''
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
    
