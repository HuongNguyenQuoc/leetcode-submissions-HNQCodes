class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Permutation trong bài này = anagram + substring liên tiếp
        #matches đếm bao nhiêu ký tự đã đủ số lượng
        #required đếm số lượng ký tự unique trong s1
        k = len(s1)
        #base case
        if k > len(s2):
            return False
        count1 = [0] * 26
        count2 = [0] * 26
        #init window for count2
        for i in range(k):
            count1[ord(s1[i]) - 97] += 1
            count2[ord(s2[i]) - 97] += 1
        matches = 0
        required = len(set(s1))
        for i in range(26):
            matches += (1 if count1[i] > 0 and count1[i] == count2[i] else 0)
        if matches == required:
            return True
        left = 0
        for right in range(k, len(s2)):
            #add
            idx = ord(s2[right]) - 97 #97 is the code ASCII of 'a'
            if count1[idx] > 0 and count1[idx] == count2[idx]:
                matches -= 1
            count2[idx] += 1
            if count1[idx] > 0 and count1[idx] == count2[idx]:
                matches += 1
            
            #remove
            idx = ord(s2[left]) - 97
            if count1[idx] > 0 and count1[idx] == count2[idx]:
                matches -= 1
            count2[idx] -= 1
            if count1[idx] > 0 and count1[idx] == count2[idx]:
                matches += 1
            left += 1
            if matches == required:
                return True
        return False