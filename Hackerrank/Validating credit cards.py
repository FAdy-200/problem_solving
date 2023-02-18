import re
a = r"^[4-6]"
b = r"[0-9]"
c = r"[0-9]{4}"
d = r"([0-9]|-)"
e = r"-"
f = r"(\d)(\1){3,}"


n = int(input())
for i in range(n):
    x = input()
    cp = (len(re.findall(c,x)))
    dp=(len(re.findall(d,x)))
    ep=(len(re.findall(d,x))-len(re.findall(e,x)))
    ap = bool(re.match(a,x))
    bp = (len(re.findall(b,x)))
    if len(re.findall(e,x)):
        x = list(x)
        for i in range(3):
            x.remove("-")
        x="".join(x)
    fp=(bool(re.search(f,x)))
    if ap and bp == 16 == len(x) and cp == 4 and ep == 16 and not fp:
        print('Valid')
    else:
        print('Invalid')
# https://www.hackerrank.com/challenges/validating-credit-card-number/problem











