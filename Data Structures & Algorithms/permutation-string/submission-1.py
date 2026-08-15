class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k, n = len(s1), len(s2)

        s1_count = [0]*26
        window = [0]*26

        if k > n:
            return False

        for i in range(k):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        if window == s1_count:
            return True

        for i in range(k, n):
            window[ord(s2[i]) - ord('a')] += 1
            window[ord(s2[i-k]) - ord('a')] -= 1
            if window == s1_count:
                return True
        return False
