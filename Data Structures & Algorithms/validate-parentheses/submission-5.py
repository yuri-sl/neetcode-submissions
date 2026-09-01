class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dicionario = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for c in s:
            if c in dicionario:
                if not stack or dicionario[c] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack