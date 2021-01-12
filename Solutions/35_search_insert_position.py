class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        position = 0
        size = len(nums)
        if size == 0:
            return position
        
        for index, value in enumerate(nums):
            if target > value:
                position += 1 
            else:
                position = index
                break
        
        return position