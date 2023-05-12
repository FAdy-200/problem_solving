def sm(p, k, l):
    return p+l < k+l


def sma(a):
    an = []
    while len(a) != 0:
        ma = ""
        for i in range(len(a)):
            if a[i]+ma <= ma+a[i]:
                ma = a[i]
                rem = i
        an.append(ma)
        a.pop(rem)
    return an


n = int(input())
for _ in range(n):
    s = list(input())
    j = len(s) - 1
    t = True
    while j != -1 and t:
        ins = s[j]
        an = "z"
        r = None
        for k in range(j, len(s)):
            if s[k]+ins > ins+s[k]:
                t = False
                r = True
        j -= 1
    if r == None:
        print("no answer")
    else:
        z = sma(s[j + 2:])
        for i in z:
            s[j+2:] = z
            print("".join(s))

