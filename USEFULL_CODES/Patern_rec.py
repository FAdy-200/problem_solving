def getPattern(x):
    p = [x[0]]
    h = True
    while h:
        c = len(p)
        ff = x[c:c + c]
        if len(ff) < c:
            p += ff
            h = False
        elif ff == p:
            h = False
        else:
            p.append(x[c])
    return p


def getPatternWithLen(x):
    p = [x[0]]
    h = True
    i = 1
    while h:
        ff = x[i:i + i]
        if len(ff) < i:
            p += ff
            h = False
        elif ff == p:
            h = False
        else:
            p.append(x[i])
            i += 1
    return p, i


