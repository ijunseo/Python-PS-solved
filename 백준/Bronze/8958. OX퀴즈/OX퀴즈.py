#基本操作
import sys
input = sys.stdin.readline

#input 
tc = int(input())
for _ in range(tc):
    st = input().rstrip()
    l = len(st)
    score = 0
    nowsc = 1
    for i in range(l):
        if st[i] == 'O':
            score += nowsc
            nowsc += 1
        else:
            nowsc = 1
    print(score)