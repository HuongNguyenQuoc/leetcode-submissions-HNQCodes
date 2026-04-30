class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0
        
        queue = deque()
        queue.append((beginWord, 1))

        while queue:
            word, length = queue.popleft()

            if word == endWord:
                return length
            
            for i in range(len(word)):
                for code in range(ord('a'), ord('z') + 1):
                    c = chr(code)
                    newWord = word[:i] + c + word[i+1:]

                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        queue.append((newWord, length + 1))
            
        return 0