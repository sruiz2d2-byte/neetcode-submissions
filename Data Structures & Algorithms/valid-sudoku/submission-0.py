class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        list_set_columns:list[set[str]] = [set() for _ in range(9)]
        boxes3x3:dict=defaultdict(set)
        
        for row in range(9):
            set_row=set()
            for column in range(9):
                box=(row//3,column//3)
                num=board[row][column]
                if num ==".":
                    continue

                if num in set_row or num in list_set_columns[column] :
                    return False
                
                if num in boxes3x3[box]:
                    return False
                set_row.add(num)
                list_set_columns[column].add(num)

                boxes3x3[box].add(num)
        return True
                
        
            
            