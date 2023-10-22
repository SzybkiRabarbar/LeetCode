# https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie: # T: 87.07% M: 87.60%
    def __init__(self):
        self.root = dict()
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if not char in node:
                node[char] = dict()
            node = node[char]
        node['END'] = True
        
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char in node:
                node = node[char]
            else:
                return False
        return 'END' in node
            
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char in node:
                node = node[char]
            else:
                return False
        return True
    
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)