class Solution:
    def isPalindrome(self, s: str) -> bool:
        original = ""
        palind = ""
        reverse = -1
        s = s.lower()
        for w in s:
            if w.isalpha() or w.isnumeric():
                original +=w
            rev_w = s[reverse]
            if rev_w.isalpha() or rev_w.isnumeric():
                palind +=rev_w
            reverse -=1
        print(original)
        print(palind)
        return original == palind
            

        

        