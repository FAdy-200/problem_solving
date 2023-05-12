def subcheck(s, ind):
    n = len(s)

    if n % ind:
        return False
    chunks = n // ind
    for i in range(chunks):
        m1 = s[i * ind:(ind * (i + 1))]
        m2 = s[n - (i + 1) * ind:n - i * ind]
        if m1 != m2:
            return False
    return True


def solution(S):
    m = S[0]
    ans = 0
    for j in S[::-1]:
        ans += 1
        if j == m:
            goalcheck = subcheck(S, ans)
            if goalcheck:
                if ans == len(S):
                    return -1
                return ans

    return -1


print(solution("aaccbxcbxaacn"))