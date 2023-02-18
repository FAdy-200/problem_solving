#Uses python3
import sys

def isBetter(i, D):
    if (len(i) == 1 and len(D) == 1) or i == D:
        return i >= D
    if len(i) < len(D):
        a, b = i, D
    else:
        a, b = D, i
    if a in b[:len(a)]:
        if b[len(a)] > b[0]:
            z = b
        elif b[len(a)] == b[0]:
            z = b
            for j in range(len(a) + 1, len(b)):
                if b[j] > b[0]:
                    break
                elif b[j] < b[0]:
                    z = a
                    break
            if a[-1] > a[0]:
                z = a
        else:
            z = a
    else:
        z = max(a, b)
    return z == i

def largest_number(arr):
    res = ""
    while len(arr) != 0:
        D = "-"
        for i in arr:
            if isBetter(i, D):
                D = i
        res += D
        arr.remove(D)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))