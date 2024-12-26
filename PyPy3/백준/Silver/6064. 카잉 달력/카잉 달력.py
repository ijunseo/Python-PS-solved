import math
import sys
num = int(sys.stdin.readline())
def findyear(a, b, c, d):
    lcm1 = math.lcm(a, b)
    i = 0
    if a == 1 or b == 1:
        print(max(c, d))#どっちも１の時にも注意
        return 0
    if c == d:
        print(c)
        return 0
    while a * i + c <= lcm1:
        answer = a * i + c
        if (a * i + c) % b == d or (a * i + c - d) % b == 0:#orに注意
            
            print(a * i + c)
            break 
        else:
            i += 1
    if a * i + c > lcm1:
        print("-1")

for _ in range(num):
    a, b, c, d = map(int, sys.stdin.readline().split())
    findyear(a, b, c, d)