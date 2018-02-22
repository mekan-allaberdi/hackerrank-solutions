# python3
import re

if __name__ == '__main__':
    str = input()
    lowc = re.findall('[a-z]', str)
    uppc = re.findall('[A-Z]', str)
    odd = re.findall('[13579]', str)
    even = re.findall('[02468]', str)
    
    res = sorted(lowc) + sorted(uppc) + sorted(odd) + sorted(even)
    print(*res, sep='')
