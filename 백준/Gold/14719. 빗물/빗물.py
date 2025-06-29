import sys
input = sys.stdin.readline
'''
問題 : 
    2次元の世界で、幅Wの区間に高さH以下のブロックが並んで積まれています。十分な雨が降ると、ブロックの間に水がたまります。
    ブロックの高さの配列が与えられるので、水がたまる総量（1マス=1単位）を計算してください。

解法 : 
    piv = 1, 2, 3... n - 1　で
    左の最大値、右の最大値(壁の高さの最大値を示す)を求めて、
    二つの壁の中で小さいものから今の壁の高さを引くと、結局問題を満足する答えが得られる。
'''

#input
n, m = map(int, input().split())

lst = list(map(int, input().split()))

ans = 0
for i in range(1, m - 1):
    lft = max(lst[:i])
    rgt = max(lst[i + 1:])
    if min(lft, rgt) - lst[i] > 0:
        ans += min(lft, rgt) - lst[i]

print(ans)