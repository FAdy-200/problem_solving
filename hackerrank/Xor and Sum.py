# https://www.hackerrank.com/challenges/xor-and-sum/problem

# a = int(input(), 2)
# b = int(input(), 2)
a = 2
b = 10
print(a, b)
# ans = dict()
sum = a ^ b
for i in range(1, 314160):
    b = b << 1
    sum += a ^ b
    # sum = sum % (10 ** 9 + 7)
    # print(bin(a), bin(b))
    # print(bin(sum))
print(sum % (10 ** 9 + 7))
