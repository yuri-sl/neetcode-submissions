class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        flag = False
        for x in nums:
            if x not in seen:
                seen.add(x)
                continue
            else:
                flag = True
        return flag
        