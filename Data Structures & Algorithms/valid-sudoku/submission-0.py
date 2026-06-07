class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Create data structures to hold our seen numbers
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        # We use a dictionary where keys are (box_row, box_col) tuples
        boxes = {} 
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                
                # 1. Skip empty spaces
                if num == ".":
                    continue
                
                # 2. Calculate which 3x3 box we are currently in
                box_coord = (r // 3, c // 3)
                if box_coord not in boxes:
                    boxes[box_coord] = set()
                
                # 3. Check for duplicates across all three rules
                if (num in rows[r] or 
                    num in cols[c] or 
                    num in boxes[box_coord]):
                    return False
                
                # 4. If it's valid so far, add it to all three sets
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_coord].add(num)
                
        return True