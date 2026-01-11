class Twitter:
    # Min Heap
    def __init__(self):
        self.timeStamp = 0  
        self.userTweets = defaultdict(list)   
        self.userFollows = defaultdict(set)   

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append([self.timeStamp, tweetId])
        self.timeStamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        heap = []

        self.userFollows[userId].add(userId)

        for followedUser in self.userFollows[userId]:
            if followedUser in self.userTweets and self.userTweets[followedUser]:
                lastIndex = len(self.userTweets[followedUser]) - 1
                ts, tId = self.userTweets[followedUser][lastIndex]
                heapq.heappush(heap, [ts, tId, followedUser, lastIndex - 1])

        while heap and len(feed) < 10:
            ts, tId, owner, nextIdx = heapq.heappop(heap)
            feed.append(tId)

            if nextIdx >= 0:
                nextTs, nextTweet = self.userTweets[owner][nextIdx]
                heapq.heappush(heap, [nextTs, nextTweet, owner, nextIdx - 1])

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollows[followerId]:
            self.userFollows[followerId].remove(followeeId)


# Time -> O(n + logn) for getNewsFeed and O(1) for others
# Space complexity: O(N*m + N*m + N) 
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
