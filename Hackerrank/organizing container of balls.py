n = int(input())
for _ in range(n):
    llkg = int(input())
    rows = []
    columns = [0]*llkg
    for k in range(llkg):
        x = list(map(int, input().split()))
        rows.append(sum(x))
        for j in range(len(x)):
            columns[j] += x[j]
    rows.sort()
    columns.sort()
    if rows == columns:
        print("Possible")
    else:
        print("Impossible")
