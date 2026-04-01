class Twitter {
public:

    int count;
    unordered_map<int, vector<pair<int, int>>> tweetMap;
    unordered_map<int, unordered_set<int>> followMap;

    Twitter() {
        count = 0;
    }
    
    void postTweet(int userId, int tweetId) {
        tweetMap[userId].push_back({count, tweetId});
        if (tweetMap[userId].size() > 10) {
            tweetMap[userId].erase(tweetMap[userId].begin());
        }
        count--;
    }
    
    vector<int> getNewsFeed(int userId) {
        vector<int> res;
        priority_queue<
            tuple<int, int, int, int>,
            vector<tuple<int, int, int, int>>,
            greater<tuple<int, int, int, int>>
        > minHeap;
        followMap[userId].insert(userId);
        for (int followeeId : followMap[userId]) {
            if (tweetMap.count(followeeId)) {
                int index = (int)tweetMap[followeeId].size() - 1;
                auto [count, tweetId] = tweetMap[followeeId][index];
                minHeap.push({count, tweetId, followeeId, index - 1});
            }
        }
        while (!minHeap.empty() && res.size() < 10) {
            auto [count, tweetId, followeeId, index] = minHeap.top();
            minHeap.pop();
            res.push_back(tweetId);
            if (index >= 0) {
               auto [count, tweetId] = tweetMap[followeeId][index];
               minHeap.push({count, tweetId, followeeId, index - 1});
            }
        }
        return res;
    }
    
    void follow(int followerId, int followeeId) {
        followMap[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        if (followMap[followerId].count(followeeId)) {
            followMap[followerId].erase(followeeId);
        }
    }
};
