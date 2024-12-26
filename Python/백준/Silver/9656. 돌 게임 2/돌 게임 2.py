num = int(input())
ans = ((num - 1) % 4) % 2
if ans == 0:
    print("CY")
else:
    print("SK")