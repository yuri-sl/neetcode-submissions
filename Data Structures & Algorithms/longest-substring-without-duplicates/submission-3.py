class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        left = right = 0
        counter = 0
        for i,c in enumerate(s):
            if c not in hashSet:
                hashSet.add(c)
                counter = max(counter,len(hashSet))
            else:
                while c in hashSet:
                    hashSet.remove(s[left])
                    left = left + 1                  
                hashSet.add(c)
                counter = max(counter,len(hashSet))
            right += 1
        return counter

            
        