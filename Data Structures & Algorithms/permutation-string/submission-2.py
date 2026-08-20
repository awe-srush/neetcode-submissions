class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k,n = len(s1), len(s2)

        if k > n:
            return False

        s1_count= [0]*26
        window = [0]*26

        for i in range(k):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        if s1_count == window:
            return True

        for i in range(k,n):
            window[ord(s2[i]) - ord('a')] += 1
            window[ord(s2[i-k]) - ord('a')] -= 1

            if window == s1_count:
                return True
        
        return False

        