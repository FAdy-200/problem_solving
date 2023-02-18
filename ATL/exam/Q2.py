sol = {}


def subroutine(A, Y):
    if sol.get((tuple(A), Y)) is not None:
        return sol[(tuple(A), Y)]
    if len(A) == 1:
        sol[(tuple(A), Y)] = 0
        return 0
    if abs(A[0] - A[1]) == Y:
        z = max(subroutine(A[1:], Y) + 1, subroutine([A[0]] + A[2:], Y))
        sol[(tuple(A), Y)] = z
        return z
    else:
        f = max(subroutine(A[1:], Y), subroutine([A[0]] + A[2:], Y))
        sol[(tuple(A), Y)] = f
        return f


def solution(A, Y):
    return subroutine(A, Y) + 1


x = solution([1, 10, 2, 11, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], 2)
# x = solution([1, 2, 3], 1)
print(x)
