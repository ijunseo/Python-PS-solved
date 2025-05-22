import sys
input = sys.stdin.readline
import math

class Bst:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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