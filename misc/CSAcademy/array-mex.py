n = int(input())
array = list(map(int, input().split(' ')))
ans = [0]*(max(array)+1)
for i in array:
    ans[i] += 1
print(ans.index(0))

