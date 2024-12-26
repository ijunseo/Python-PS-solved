num = int(input())
num_a = (num % 10) * 10 + (num // 10 + num % 10) % 10
i = 1
while num_a != num and i < 100: 
    num_1 = num_a % 10
    num_2 = (num_a // 10)
    num_a = num_1 * 10 + (num_2 + num_1) % 10 
    i += 1
print(i)