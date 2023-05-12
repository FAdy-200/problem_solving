# https://leetcode.com/problems/product-of-array-except-self/


def productExceptSelf(nums):
    prod = [0] * len(nums)
    p = nums[0]
    for i in range(1, len(nums)):
        prod[i] = p
        p *= nums[i]
    p = nums[len(nums)-1]
    for i in range(len(nums) - 2, 0, -1):
        prod[i] *= p
        p *= nums[i]
    prod[0] = p
    return prod


def npProductExceptSelf(nums):
        import numpy as np
        nums = np.array(nums)
        prod = np.zeros(nums.size)
        p = nums[0]
        for i in range(1, len(nums)):
            prod[i] = p
            p *= nums[i]
        p = nums[len(nums)-1]
        for i in range(len(nums) - 2, 0, -1):
            prod[i] *= p
            p *= nums[i]
        prod[0] = p
        return prod
# nums = [1, 2, 3, 4]
nums = [-1,1,0,-3,3]



print(productExceptSelf(nums))
