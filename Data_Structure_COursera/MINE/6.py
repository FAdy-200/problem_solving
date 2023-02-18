# Uses python3

def sum_fast(n):
    s = int((- 1 + (8*n + 1) ** 0.5) // 2)
    a = []    
    for i in range(1, s):
        a.append(i)
    a.append(int(n - (s) * (s-1) /2))
    return a

if __name__ == '__main__':
    n = int(input())
    ans = sum_fast(n)
    print(len(ans))
    for x in ans:
        print(x, end=' ')