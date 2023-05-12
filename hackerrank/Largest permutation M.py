o = open("testCases.txt", "r")
out = open("output.txt", "r")


def largestPermutation(k, arr):
    d = {key: v for v, key in enumerate(arr)}
    for i in range(k):
        if i == 8076 or len(arr) - i == 8076:
            print("asd")
            print()
        if arr[i] == len(arr) - i:
            continue
        else:
            zz = arr[i]
            gg = arr[d[len(arr) - i]]
            arr[i], arr[d[len(arr) - i]] = arr[d[len(arr) - i]], arr[i]
            d[zz], d[gg] = d[gg], d[zz]
    return arr


n, k = map(int, o.readline().split())
x = list(map(int, o.readline().split()))
z = (largestPermutation(k, x))
ans = list(map(int, out.readline().split()))
for i in range(n):
    if ans[i] != z[i]:
        print("index ",i)
        print("ans ",ans[i])
        print("try ",z[i])
# for i in z:
#     print(i, end=" ")
