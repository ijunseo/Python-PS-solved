a,b=map(int,input().split())
if b - 45 < 0:
    if a == 0:
        a, b = 23, 60+(b-45)
    else:
        a, b = a-1, 60+(b-45)
else:
    b -= 45
print(a, b)