from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.dict_list:dict[str,list[tuple[str,int]]]=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.dict_list[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:

        size=len(self.dict_list[key])-1
        left=0
        right=size

        while left<=right:
            mid=(left+right)//2


            if self.dict_list[key][mid][1]>timestamp:
                right=mid-1
            else:
                left=mid+1
        if left==0:
            return ""

        return self.dict_list[key][left-1][0]



            

