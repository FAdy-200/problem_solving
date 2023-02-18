# python3
import sys

def compute_min_refills(d, m, s):
    stops = [0] + s + [d]
    current = total = 0
    n = len(stops)
    while True:
        last = current
        for i in range(current + 1 , n):
            if stops[i] - stops [last] <= m:
                current = i
            else:
                break
        if last == current:
            return -1
        if current == n-1:
            return total
        total += 1

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
