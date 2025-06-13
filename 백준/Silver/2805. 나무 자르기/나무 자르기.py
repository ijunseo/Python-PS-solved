import sys
input = sys.stdin.readline

n, m  = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort(reverse= True)

mi, mx = 1 , max(lst)

ans = 0
while mi <= mx:
    #print(mi, mx)
    ans = 0
    piv = (mi + mx) // 2
    #print(piv)

    for nums in lst:
        if nums > piv:
            ans += nums - piv
        else:
            break
    #print(ans, 'ans')
    
    if ans < m:
        mx = piv - 1
    else:
        mi = piv + 1

print(mx)