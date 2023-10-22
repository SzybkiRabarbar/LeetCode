# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class WordDictionary: # T: 84.77% M: 92.46%
    def __init__(self):
        self.root = dict()
    
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if not char in node:
                node[char] = dict()
            node = node[char]
        node['END'] = True
        
    def search(self, word: str, node = None) -> bool:
        if not node:
            node = self.root
        for i, char in enumerate(word):
            
            if char == '.':
                for key in node.keys():
                    if key == 'END':
                        continue
                    if len(word) <= i + 1:
                        r = self.search('', node[key])
                    else:
                        r = self.search(word[i + 1:], node[key])
                    if r:
                        return True
                return False
            
            elif char in node:
                node = node[char]
            else:
                return False
        return 'END' in node
    
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)