class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        values = dict()

        for i in range(len(nums)):
            current = nums[i]
            difference = target - current
            if difference in values.keys():
                return [values[difference],i]

            else:
                values[current] = i
        
        
