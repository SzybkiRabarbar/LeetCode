# https://leetcode.com/problems/clone-graph/

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque, defaultdict

class Solution: # T: 58.74% M: 91.92%
    def cloneGraph(self, node: Node) -> Node:
        if node is None:
            return node

        nodes_map = defaultdict(Node)
        nodes_map[node] = Node(node.val)
        q = deque([node])

        while q:
            n = q.popleft()
            for neighbor in n.neighbors:
                if neighbor not in nodes_map:
                    nodes_map[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                nodes_map[n].neighbors.append(nodes_map[neighbor])

        return nodes_map[node]
