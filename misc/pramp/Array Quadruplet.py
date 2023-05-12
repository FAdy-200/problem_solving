# https://www.pramp.com/challenge/gKQ5zA52mySBOA5GALj9

def subroutine(arr, s):
    i = 0
    j = len(arr) - 1
    last = [0, 0]
    while j > i:
        temp = arr[i] + arr[j]
        if temp > s:
            j -= 1
            last = [0, 1]
        if temp < s:
            i += 1
            last = [-1, 0]
        if temp == s:
            return arr[i], arr[j]
    return arr[i + last[0]], arr[j + last[1]]


def find_array_quadruplet(arr, s):
    arr = list(sorted(arr))
    k = 0
    h = len(arr) - 1
    if h < 3:
        return []
    while  h > k:
        t1 = arr[k]
        t2 = arr[h]
        if t2 + t1 > s:
            h -= 1
            continue
        s2 = s - t2 - t1
        temp = subroutine(arr[0:k]+arr[k+1:h]+arr[h+1:], s2)
        ans = t1 + t2 + temp[0] + temp[1]
        if ans > s:
            h -= 1
        elif ans < s:
            k += 1
        else:
            return list(sorted([t1, t2, temp[0], temp[1]]))
    return []


x = find_array_quadruplet([4, 4, 2, 2], 12)

print(x)
