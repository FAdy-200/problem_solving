# Uses python3

def optimal_points(a, b):
    X, Z = a.copy(), b.copy()
    n = len(b)
    
    for i in range(n):
        e = b.index(max(b))
        X[i] = a[e]
        Z[i] = b[e]
        b[e] = 0
        
    X = X[::-1]
    Z = Z[::-1]
    P = []

    for i in range(n):
        c = 0
        for j in range(len(P)):
            if P[j] >= X[i] and P[j] <= Z[i]:
               c = 1
        if c == 0:
            P.append(Z[i])
    return P

n = 3
v = [1,2,3]
w = [3,5,6]
for i in range(1000):
    optimal_points(v, w)
