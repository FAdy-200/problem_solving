def sol1(A):
    a = A
    def helper(i,even):
        if i == len(a):
            return 0
        num = a[i] if even else -a[i]
        no = helper(i+1,even)
        even *=-1
        taken = helper(i+1,even) + num
        return max(no,taken)
    return helper(0,1)


x = [4, 1 ,2 ,3]
print(sol1(x))