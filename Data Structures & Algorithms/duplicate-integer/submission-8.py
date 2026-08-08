class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            # val = nums[i]  # You can keep or remove this; nums[i] works directly
            for j in range(i + 1, len(nums)):
                if nums[j] == nums[i]:
                    return True # Found a duplicate!
        
        # If we get here, it means we checked every pair and found nothing
        return False

