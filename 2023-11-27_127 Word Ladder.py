# https://leetcode.com/problems/word-ladder/

from collections import defaultdict, deque

class Solution: # T: 55.25% M: 6.23%
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        similarities_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)): similarities_dict[word[0:i] + '_' + word[i+1:]].append(word[i])

        seen = set()
        result = 0
        was_found = False
        que = deque([beginWord])
        while que and not was_found:
            result += 1
            for _ in range(len(que)):
                word = que.popleft()
                if word in seen:
                    continue
                else:
                    seen.add(word)
                if word == endWord:
                    was_found = True
                    break
                for i in range(len(word)):
                    characters = similarities_dict[word[0:i] + '_' + word[i+1:]]
                    for char in characters:
                        que.append(word[0:i] + char + word[i+1:])
        
        return result if was_found else 0