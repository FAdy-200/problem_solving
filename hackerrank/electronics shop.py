l = list(map(int, input().split()))
k = list(map(int, input().split()))
m = list(map(int, input().split()))
x=[]
for i in range(len(k)):
    for j in range(len(m)):
        if k[i] + m[j] <= l[0]:
            x.append(k[i]+m[j])
if len(x) != 0:
    print(max(x))
else:
    print(-1)








































































