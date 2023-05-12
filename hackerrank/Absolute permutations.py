bnn = int(input())
xl = [str(__) for __ in range(1, (10**5)+1)]
for _ in range(bnn):
    n, m = map(int, input().split())
    x = xl[:n]
    # x = [str(i) for i in range(1, n + 1)]
    if m == 0:
        print(" ".join(x))
    elif (n / m) % 2 == 0:
        # print(n % m % 2)
        # x = " ".join(x)
        ans = ""
        for i in range(0, (n//m), 2):
            z = x[(i+1)*m:(i+2)*m]+x[i*m:(i+1)*m]+[""]
            # print(z)
            # ans += " ".join(list((map(str, z))))
            ans += " ".join(z)
        print(ans)
    else:
        print(-1)
