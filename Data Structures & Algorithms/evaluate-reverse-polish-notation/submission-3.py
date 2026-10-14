class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr=[]
        
        for token in tokens:

            if token == "+":
                b = int(arr.pop())
                a = int(arr.pop())
                arr.append(a + b)
            elif token == "-":
                b = int(arr.pop())
                a = int(arr.pop())
                arr.append(a - b)
            elif token=="*":
                b = int(arr.pop())
                a = int(arr.pop())
                arr.append(a * b)
            elif token=="/":
                b = int(arr.pop())
                a = int(arr.pop())
                arr.append(int(a / b))
            else:
                arr.append(int(token))
        
        return arr[0]
