#python3

'''
input : 
    add <contact>
    find <contact>
output:
    on find operation , print contact occurrence count
'''

_count = 'count'

def add_trie(root, word):
    current_dict = root
    for letter in word:
        current_dict = current_dict.setdefault(letter, {})
        count = current_dict.setdefault(_count, 0)
        current_dict[_count] = count + 1
    return root

def find_contact(root, contact):
	current_dict = root
	for letter in contact:
		current_dict = current_dict.get(letter, None)
		if current_dict == None:
			return 0

	return current_dict[_count]

if __name__ == '__main__':
    root = dict()
    n = int(input().strip())
    for _ in range(n):
        cmd, contact = input().strip().split()
        if cmd == 'add':
            root = add_trie(root, contact)
        else:
            print(find_contact(root, contact))
