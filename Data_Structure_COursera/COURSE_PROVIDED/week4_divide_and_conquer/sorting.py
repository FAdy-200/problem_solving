def srt_bi(a, b):
    for i in range(len(b)):
        l, r = 0, len(a)
        mo = -1
        while r >= l:
            mid = ((l + r) // 2)
            if b[i] >= a[mid]:
                l = mid
                c = True
            elif b[i] < a[mid]:
                r = mid
                c = False
            if mo == mid:
                if c:
                    a.insert(mid + 1, b[i])
                else:
                    a.insert(mid, b[i])
                break
            mo = mid
    return a


def srt(a, b):
    """

    :param a:
    :param b:
    :return: merge sort a,b
    faster by 55% than srt_bi
    """
    m = len(a)
    n = 0
    f = True
    for i in range(len(b)):
        while n < len(a):
            if b[i] <= a[n]:
                a.insert(n, b[i])
                f = False
                n += 1
                d = i
                break
            n += 1
        if n == len(a) and f:
            a = a + b
            d = -1
            break
    if len(a) != m + len(b):
        a = a + (b[d + 1:])
    return a


def quick_sort(a):
    """

    :param a:
    :return: sorted a
    faster by about 55% than quick_sort_bi
    """
    if len(a) == 1:
        return a
    return srt(quick_sort(a[len(a) // 2:]), quick_sort(a[:len(a) // 2]))


def quick_sort_bi(a):
    if len(a) == 1:
        return a
    return srt_bi(quick_sort_bi(a[len(a) // 2:]), quick_sort_bi(a[:len(a) // 2]))


n = int(input())
# n = 0
if n:
    a = list(map(int, input().split()))
    # import numpy as np
    # for i in range(10):
    #     print(i)
    #     a = list(np.random.choice(1000000000, np.random.randint(low=1, high=100000), replace=True))
    # z = quick_sort_bi(a)
    h = quick_sort(a)
    print(" ".join(list(map(str, h))))
    # print(" ".join(list(map(str, z))))
else:
    import numpy as np
    import pandas as pd

    z = []
    for i in range(
            int(input())
    ):
        print(i)
        h = []
        a = list(np.random.choice(1000000000, np.random.randint(low=1, high=100000), replace=True))
        h.append(sorted(a))
        h.append(quick_sort(a))
        h.append(a)
        z.append(h)
    ss = pd.DataFrame(z, columns=["r", "m", "A"])
    ss["c"] = ss["r"] == ss["m"]
    ss = ss[["r", "m", 'c', 'A']]
    ss = ss[ss["c"] == False]
    print(ss)
