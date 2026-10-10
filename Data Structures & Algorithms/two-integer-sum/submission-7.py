class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return None
        # [3,4,5,6], target = 7
        dict_needed = {}
        for i,num in enumerate(nums):
            needed = target - num
            if num in dict_needed:
                return [dict_needed[num], i]
            else:
                dict_needed[needed] = i
        return []