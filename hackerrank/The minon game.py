import re


def minion_game(x):
    p = r"[AEIOU]"
    iter = re.finditer(p, x)
    z = [m.start(0) for m in iter]
    le = len(x)
    xt = int((le*(le+1))/2)
    k = 0
    for i in z:
        k += le - i
    s = xt - k

    if s > k:
        print('Stuart {}'.format(s))
    elif k > s:
        print('Kevin {}'.format(k))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)



# https://www.hackerrank.com/challenges/the-minion-game/problem