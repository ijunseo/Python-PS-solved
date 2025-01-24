#基本操作
import sys
input = sys.stdin.readline

#入力
st1 = input().rstrip()
target = input().rstrip()

#KMPlist
jumplist = [0 for _ in range(len(target))]
j = 0
for i in range(1, len(target)):
    while j > 0 and target[i] != target[j]:
        j = jumplist[j - 1]
    if target[i] == target[j]:
        j += 1
        jumplist[i] = j 
        
# #solve(KMP)
ans = []
piv = 0 
for i in range(len(st1)):

    while piv > 0 and st1[i] != target[piv]:
        piv = jumplist[piv - 1]

    if st1[i] == target[piv]:
        if piv == len(target) - 1:#一致する
            ans.append(i - len(target) + 2)
            piv = jumplist[piv]
        else:
            piv += 1

print(len(ans))
print(*ans)