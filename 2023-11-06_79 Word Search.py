# https://leetcode.com/problems/word-search/

class Solution: # T: 87.46% M: 10.91%
    def exist(self, board: list[list[str]], word: str) -> bool:
        def spider(path: set, pointer, i, j):
            if pointer == len(word):
                return True
            
            path.add((i, j))
            if i > 0 and not (i - 1, j) in path and board[i - 1][j] == word[pointer]:
                if spider(path, pointer + 1, i - 1 , j):
                    return True
            
            if j > 0 and not (i, j - 1) in path and board[i][j - 1] == word[pointer]:
                if spider(path, pointer + 1, i, j - 1):
                    return True
            
            if i < len(board) - 1 and not (i + 1, j) in path and board[i + 1][j] == word[pointer]:
                if spider(path, pointer + 1, i + 1, j):
                    return True
            
            if j < len(board[0]) - 1 and not (i, j + 1) in path and board[i][j + 1] == word[pointer]:
                if spider(path, pointer + 1, i, j + 1):
                    return True
            path.remove((i, j))
            return False
        
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char == word[0]:
                    if spider(set(), 1, i, j):
                        return True
        return False