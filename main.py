def removeElement(self, nums: List[int], val: int) -> int:
    total = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[total] = nums[i]
            total += 1
    return total
