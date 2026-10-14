class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr=[]
        
        for token in tokens:

            if token in {"+", "-", "*", "/"}:
                b = int(arr.pop())
                a = int(arr.pop())
                if token == "+":
                    arr.append(a + b)
                elif token == "-":
                    arr.append(a - b)
                elif token=="*":
                    arr.append(a * b)
                elif token=="/":
                    arr.append(int(a / b))
            else:
                arr.append(int(token))
        
        return arr[0]
