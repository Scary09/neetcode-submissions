class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stored={}
        for i in (nums):
            if i in stored:
                return True
            else:
                stored[i]=0
        return False