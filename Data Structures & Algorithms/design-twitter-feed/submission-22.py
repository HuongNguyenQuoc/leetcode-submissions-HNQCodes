class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        res = []
        users_to_check = self.following[userId] | {userId}

        for uuid in users_to_check:
            tweet_list = self.tweets[uuid]
            if tweet_list:
                idx = len(tweet_list) - 1
                time, tweetId = tweet_list[idx]
                heapq.heappush(maxHeap, (-time, tweetId, uuid, idx -1))
        
        while maxHeap and len(res) < 10:
            time, tweetId, uuid, idx = heapq.heappop(maxHeap)
            res.append(tweetId)
            if idx >= 0:
                next_time, next_tweetId = self.tweets[uuid][idx]
                heapq.heappush(maxHeap, (-next_time, next_tweetId, uuid, idx - 1))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
