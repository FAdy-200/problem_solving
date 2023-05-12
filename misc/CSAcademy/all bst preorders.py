# Parameter size is an integer
# The function should not return anything
# Use "print" to flush your solutions
def all_bst_preorders(size):
    import itertools
    x = [i for i in range(1,size+1)]
    z = itertools.product(x, x)
    for i in z:
        print(" ".join(list(map(str, i))))
###
size = int(input())
all_bst_preorders(size)
#TODO: finish this
