# Uses python3

def get_change(m):
    b10 = m//10
    m = m % 10
    b5 = m//5
    m = m % 5
    b1 = m
    # write your code here
    return b1+b5+b10


n = int(input())
print(get_change(n))














