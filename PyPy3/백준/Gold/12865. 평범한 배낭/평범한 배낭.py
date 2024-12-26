num, bag_w = map(int, input().split())
knap_list = list(0 for i in range(bag_w + 1))
val_list = []
for i in range(num):
  a, b = map(int, input().split())
  val_list.append((a, b))

dp_matrix = []

dp_matrix = [0] * (bag_w + 1)
dp_matrix_copy = dp_matrix.copy()
for i in range (num):
  for j in range(bag_w + 1 - val_list[i][0]):
    dp_matrix[j + val_list[i][0]] = max(dp_matrix_copy[j + val_list[i][0]], dp_matrix_copy[j] + val_list[i][1])
  dp_matrix_copy = dp_matrix.copy()
print(dp_matrix[bag_w])
