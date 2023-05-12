import math

x = list(map(int, input().split()))
k = x[0] * x[1]
q = math.floor(k/4)
m = (k-q*4)
w = math.floor(m/2)
e = m-w*2
print(q+w+e)





