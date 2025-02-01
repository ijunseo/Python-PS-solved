#基本操作
import sys
input = sys.stdin.readline

#input 
n = int(input())
katamuki_1 = set()
katamuki_2 = set()
div0 = set()
for _ in range(n):
    x, y = map(int, input().split())
    if x > 0:
        katamuki_1.add(y/x)
    elif x < 0:
        katamuki_2.add(y/x)
    else:
        if y > 0:
            div0.add(1)
        else:
            div0.add(-1)

#output
print(len(katamuki_1) + len(katamuki_2) + len(div0))