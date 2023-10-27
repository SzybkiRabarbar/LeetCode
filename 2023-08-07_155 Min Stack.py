#https://leetcode.com/problems/min-stack/
'''
class MinStack(object): ## T: 17.65% M: 93.49%

    def __init__(self):
        self.content = []

    def push(self, val: int) -> None:
        self.content.append(val)
        
    def pop(self) -> None:
        self.content.pop()

    def top(self) -> int:
        return self.content[len(self.content)-1]

    def getMin(self) -> int:
        return min(self.content)
'''
'''
import numpy as np
class MinStack(object): ## T: 20.54% M: 5.06% 2-times faster than wihout np

    def __init__(self):
        self.content = np.array([])
        self.content = self.content.astype(np.int16)

    def test(self):
        print(self.content)
    
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.content = np.append(self.content, val)
        
    def pop(self):
        """
        :rtype: None
        """
        self.content = self.content[0:-1]
        
    def top(self):
        """
        :rtype: int
        """
        return self.content[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return np.min(self.content)
'''
#@Swap24 https://leetcode.com/Swap24/
class MinStack: ## T: 92.9% M: 79.25% 

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.currentMin = float('inf')
        self.prevMins = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        if x <= self.currentMin:
            self.prevMins.append(self.currentMin)
            self.currentMin = x

    def pop(self) -> None:
        if self.stack[-1] == self.currentMin:
            self.currentMin = self.prevMins.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.currentMin
    