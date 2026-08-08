class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_tuple=set(nums)
        if len(nums)==len(my_tuple):
            return False
        else:
            return True