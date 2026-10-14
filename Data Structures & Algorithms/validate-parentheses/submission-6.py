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
            elif arr:
                if char == arr[-1]:
                    arr.pop()
                else:
                    return False
            else:
                return False

        return len(arr)==0
