class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        #Init a dictionary empty so that each characters in elements words
        adj = {c : set() for word in words for c in word}

        #Create a graph about connect each character
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1] 
            minLen = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            elif (word1[:minLen] != word2[:minLen]):
                for j in range(minLen):
                    if word1[j] != word2[j]:
                        adj[word1[j]].add(word2[j])
                        break

        #Init visit for save each key have value True or False of current path: False = visited, True= current path
        visit = {}
        #Init res and at the end use return join
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)
            return visit[c]

        for c in adj:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)