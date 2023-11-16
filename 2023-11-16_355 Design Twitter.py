# https://leetcode.com/problems/design-twitter/

import heapq

class Twitter: # T: 29.81% M: 8.31%
    def __init__(self):
        self.order = 0
        self.users_data = dict() # {user_id: [posts_list[(order,post_id)], followed_list[user_id]]}
    
    def check_if_exits(self, userId):
        if not userId in self.users_data:
            self.users_data[userId] = ([], set())
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.check_if_exits(userId)
        self.users_data[userId][0].append((self.order, tweetId))
        self.order += 1
        
    def getNewsFeed(self, userId: int) -> list[int]:
        self.check_if_exits(userId)
        feed = self.users_data[userId][0][-10:]
        heapq.heapify(feed)
        for followed_user in self.users_data[userId][1]:
            for post in self.users_data[followed_user][0][-10:]:
                heapq.heappush(feed, post)
                if len(feed) > 10:
                    heapq.heappop(feed)
        
        result = []
        for _ in range(len(feed)):
            result.append(heapq.heappop(feed)[1])
        return result[::-1]
        
            
    def follow(self, followerId: int, followeeId: int) -> None:
        for user_id in [followerId, followeeId]:
            self.check_if_exits(user_id)
        
        self.users_data[followerId][1].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        for user_id in [followerId, followeeId]:
            self.check_if_exits(user_id)
        try:
            self.users_data[followerId][1].remove(followeeId)
        except KeyError:
            pass
        
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)