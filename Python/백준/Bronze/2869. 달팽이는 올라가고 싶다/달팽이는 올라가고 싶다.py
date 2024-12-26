import math
a , b , v = map(int,input().split())
last_high = v - a
day = math.ceil(last_high / (a - b) )
print(day + 1)