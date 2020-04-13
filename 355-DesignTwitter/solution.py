class Twitter:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.time += 1
        self.tweets[userId].append((tweetId, self.time))
        
    def sortSecond(self,val): 
        return val[1]  

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        users = self.user[userId]
        users.add(userId)
        tweettmp = []
        temp = []
        for u in users:
            tweettmp.append(self.tweets[u][-10:])
        for u in tweettmp:
            for t in u:
                temp.append(t)
        temp.sort(key= self.sortSecond, reverse=True)
        return [item[0] for item in temp[:10]]
        
       
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.user[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.user[followerId]:
            self.user[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
