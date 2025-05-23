import sys
input = sys.stdin.readline
import math

'''
解法：
l_weight = 左のサブ木の属するノードの数
r_weight = 右のサブ木の属するノードの数

l_val = 左のサブ木を構成する場合の数
r_val = 左のサブ木を構成する場合の数

漸化式：
現在のノードを構成する場合の数 = (l_weight H r_weight) * (l_val * r_val)
Hは重複組み合わせを示す

まず、inputが`2 1 4 3 5`のように数字の入力順なので
BSTのClassを作成して二分木Classを作って
make_treeでノードを追加しながら二分木を作成

また、実装はpostorderでchild -> parent順に探索しながら値を更新するように設計した
'''
class Bst:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def make_tree(nownode, nownum):
    if nownode == nownum:
        return

    weight[nownode.value] += 1

    if nownum < nownode.value:
        if nownode.left == None:
            nownode.left = Bst(nownum)
        else:
            make_tree(nownode.left, nownum)
    else:
        if nownode.right == None:
            nownode.right = Bst(nownum)
        else:
            make_tree(nownode.right, nownum)

#input
tc = int(input())
for _ in range(tc):
    n = int(input())
    if not n: # n == 0なら終了
        sys.exit()

    line = [[] for _ in range(n + 1)]
    lst = list(map(int, input().split()))
    weight = [1] * (n + 1)
    val_lst = [1] * (n + 1)

    tree = Bst(lst[0])
    for i in range(1, n):
        now = lst[i]
        make_tree(tree, lst[i])

    def find_ans(now_node):
        if now_node.left != None:
            find_ans(now_node.left)
        if now_node.right != None:
            find_ans(now_node.right)

        l_weight = weight[now_node.left.value] if now_node.left else 0
        r_weight = weight[now_node.right.value] if now_node.right else 0

        l_val = val_lst[now_node.left.value] if now_node.left else 1
        r_val = val_lst[now_node.right.value] if now_node.right else 1


        val_lst[now_node.value] = (
            math.comb(l_weight + r_weight, l_weight) * l_val * r_val
        ) % 9999991

        weight[now_node.value] = l_weight + r_weight + 1
    find_ans(tree)
    print(val_lst[tree.value])