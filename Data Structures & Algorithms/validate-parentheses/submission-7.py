class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dicionario = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for c in s:
            #Closing bracket
            if c in dicionario.keys():
                if not stack or dicionario[c] != stack[-1]:
                    return False
                stack.pop()
            #Opening bracket
            else:
                stack.append(c)
        return not stack