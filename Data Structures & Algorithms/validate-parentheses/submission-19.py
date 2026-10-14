class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        arr=[]
        for char in s:

            
            if char in brackets:
                arr.append(brackets[char])
            elif not arr or char != arr[-1]:
                return False
            else:
                arr.pop()

            
        return not arr
