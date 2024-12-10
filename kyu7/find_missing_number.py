def missing_no(nums):
    for i in range(0,101):
        if i not in [val for val in nums]:
            return i
        