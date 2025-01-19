#基本操作
#union find 練習
import sys
input = sys.stdin.readline

#入力
dot, qnum = map(int, input().split())#点の数、橋掛ける数

linkedlist = [i for i in range(dot)]#あるグループに点が属しているかを確認


#アルゴリズム
#find
def find(now):#nowのparentnodeを探す
	if linkedlist[now] != now:#今のparentnodeが自分ではないと
		return find(linkedlist[now])#parentnodeを探す
	return now

#union
def union(one, two, time):#dot one, dot two, 入力回数
	par_one = find(one)
	par_two = find(two)
	if par_one < par_two:
		linkedlist[par_two] = par_one
	elif par_one > par_two:
		linkedlist[par_one] = par_two#parentsnodeのindexが小さい方に合わせる
	else:#parentnodeが一致する（サイクル完成）
		print(time)
		sys.exit()
		

for i in range(1, qnum + 1):
	dot1, dot2 = map(int,input().split())
	union(dot1, dot2, i)

print('0') #サイクルがない