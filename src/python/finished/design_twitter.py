import heapq
from collections import defaultdict
from typing import List


class Twitter:
    def __init__(self):
        self.timestamp = 0
        # Dict<ID, List<(TweetId, Timestamp)>>
        self.user_posts = defaultdict(list)
        # Dict<ID, Set<ID>>
        self.user_follows = defaultdict(set)

    def time(self) -> int:
        t = self.timestamp
        self.timestamp += 1
        return t

    def postTweet(self, userId: int, tweetId: int) -> None:
        posts = self.user_posts[userId]
        t = self.time()
        posts.append((tweetId, t))
        self.user_posts[userId] = posts

    def getNewsFeed(self, userId: int) -> List[int]:
        feed_srcs = set(self.user_follows[userId])
        feed_srcs.add(userId)

        feed = []
        for uid in feed_srcs:
            recent_user_posts = self.user_posts[uid][-10:]
            for tid, t in recent_user_posts:
                heapq.heappush(feed, (t, tid))
                if len(feed) > 10:
                    heapq.heappop(feed)

        feed.sort(key=lambda p: -p[0])
        return [tid for _, tid in feed]

    def follow(self, followerId: int, followeeId: int) -> None:
        fset = self.user_follows[followerId]
        fset.add(followeeId)
        self.user_follows[followerId] = fset

    def unfollow(self, followerId: int, followeeId: int) -> None:
        fset = self.user_follows[followerId]
        if followeeId in fset:
            fset.remove(followeeId)
            self.user_follows[followerId] = fset


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
