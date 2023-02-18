# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    val = 0
    n = len(values)
    w, v, r = [0]*n, [0]*n, [0]*n

    for i in range(n):
        r[i] = values[i] / weights[i]
        
    for i in range(n):
        e = r.index(max(r))
        v[i] = values[e]
        w[i] = weights[e]
        r[e] = 0

    for i in range(n):
        if capacity == 0 :
            return val
        c = min(capacity, w[i])
        capacity -= c
        val += c * v[i] / w[i]
    return val


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
