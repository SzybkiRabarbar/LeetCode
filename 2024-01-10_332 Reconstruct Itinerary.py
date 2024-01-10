# https://leetcode.com/problems/reconstruct-itinerary/

class Solution:  # T: 91.72% M: 8.40%
    # @ https://www.youtube.com/watch?v=ZyB_gQ8vqGA
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        adj = {src: [] for src, dst in tickets}
        res = []

        for src, dst in tickets:
            adj[src].append(dst)

        for key in adj:
            adj[key].sort()

        def dfs(adj, result, src):
            if src in adj:
                destinations = adj[src][:]
                while destinations:
                    dest = destinations[0]
                    adj[src].pop(0)
                    dfs(adj, res, dest)
                    destinations = adj[src][:]
            res.append(src)

        dfs(adj, res, "JFK")
        res.reverse()

        if len(res) != len(tickets) + 1:
            return []

        return res
