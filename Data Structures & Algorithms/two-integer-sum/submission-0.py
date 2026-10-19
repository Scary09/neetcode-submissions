class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        passed={}
        for i in range(len(nums)):
            curr_num=nums[i]
            secc_num=target-curr_num
            if secc_num in passed:
                return[passed[secc_num],i]
            passed[curr_num]=i
