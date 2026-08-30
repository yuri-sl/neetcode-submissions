class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_k = {}
        for n in nums:
            if n not in top_k:
                top_k[n]=1
            else:
                top_k[n]=top_k[n]+1
        sorted_dic = dict(sorted(top_k.items(),key=lambda x: x[1],reverse=True))
        ans = [x for x in list(sorted_dic)[:k]]
        return ans
        
        