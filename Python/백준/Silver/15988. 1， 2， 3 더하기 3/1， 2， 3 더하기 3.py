import sys
num_list = [0, 1, 2, 4]

miss = int(input())
while True:
    try:
        a = int(sys.stdin.readline())
        try:
            print(num_list[a])
        except:
            while(len(num_list) != a + 1):
                a1 = num_list[-1] % 1000000009
                a2 = num_list[-2] % 1000000009
                a3 = num_list[-3] % 1000000009
                num_list.append((a1 + a2 + a3) % 1000000009)
            print(num_list[a])
    except:
        sys.exit()