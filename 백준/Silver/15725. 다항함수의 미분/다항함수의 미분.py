#基本操作
import sys
input = sys.stdin.readline

#input 
inp = input()
lst = []
if inp[0] == 'x':
    print(1)
    sys.exit()
if inp[0] == '-':
    if inp[1] == 'x':
        print('-1')
        sys.exit()
for i in range(len(inp)):
    if inp[i] != 'x':
        lst.append(inp[i])
    elif inp[i] == 'x':
        for i in lst:
            print(i, end = '')
        sys.exit()
print(0)
