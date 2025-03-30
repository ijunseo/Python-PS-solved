#基本操作
import sys
input = sys.stdin.readline
import heapq


#input 
n = int(input())
q = []

#原点から近い順でheappush
for _ in range(n):
    loc, fuel = map(int, input().split())
    heapq.heappush(q, (loc, fuel))

target, now_fuel = map(int, input().split())

#現段階で使える燃料
fuel_list = []

use = 0
while True:
    if target <= now_fuel:
        print(use)
        sys.exit()
    
    if q:
        next_fuel_loc = q[0][0]
    else:
        next_fuel_loc = 10 ** 7
    
    if next_fuel_loc <= now_fuel:
        next_fuel_loc, nextfuel = heapq.heappop(q)
        #大きい順に入れたいので -1 をかける
        heapq.heappush(fuel_list, - nextfuel)

    else:
        #使える燃料がないかつ次のガススタンドまで行けない
        if not fuel_list:
            print('-1')
            sys.exit()
        
        use += 1
        use_fuel = heapq.heappop(fuel_list)
        now_fuel += - use_fuel