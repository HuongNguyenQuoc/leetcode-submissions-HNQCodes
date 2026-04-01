class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        k = len(s1)
        if k > len(s2):
            return False

        count1 = [0]*26
        count2 = [0]*26

        for c in s1:
            count1[ord(c)-97] += 1

        required = sum(1 for x in count1 if x > 0)
        matches = 0

        # init window
        for i in range(k):
            idx = ord(s2[i])-97
            count2[idx]+=1

        for i in range(26):
            if count1[i] > 0 and count1[i]==count2[i]:
                matches+=1

        if matches == required:
            return True

        left = 0

        for right in range(k, len(s2)):

            # add
            idx = ord(s2[right])-97
            if count1[idx] > 0 and count2[idx]==count1[idx]:
                matches-=1
            count2[idx]+=1
            if count1[idx] > 0 and count2[idx]==count1[idx]:
                matches+=1

            # remove
            idx = ord(s2[left])-97
            if count1[idx] > 0 and count2[idx]==count1[idx]:
                matches-=1
            count2[idx]-=1
            if count1[idx] > 0 and count2[idx]==count1[idx]:
                matches+=1

            left+=1

            if matches==required:
                return True

        return False
