# Uses python3
def summands(n):
    """

    :type n: int

    """
    if n <= 2:
        return 1, [str(n)]
    else:
        v = [1]
        i = 2
        n -= 1
        h = True
        while h:
            if n-i <= v[-1] or n-i == 0:
                if n == v[-1]:
                    v.pop(0)
                    n += 1
                v.append(int(n))
                return len(v), list(map(str, v))
            else:
                n = n-i
                v.append(i)
                i += 1










n = int(input())
x = summands(n)
print(x[0])
print(" ".join(x[1]))









