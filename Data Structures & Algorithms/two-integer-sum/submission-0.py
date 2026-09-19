class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashMap = {}
        for i in range(0,n):
            remaining = target - nums[i]
            if remaining in hashMap:
                return [hashMap[remaining], i]
            hashMap[nums[i]] = i    



        
        