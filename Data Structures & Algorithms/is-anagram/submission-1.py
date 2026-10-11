class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        Ssorted = sorted(s)
        Tsorted = sorted(t)
        return Ssorted == Tsorted
        
        # count = {}

        # if len(s) != len(t):
        #     return False

        # for char in s:
        #     if char in count:
        #         count[char] += 1
        #     else:
        #         count[char] = 1

        # for char in t:
        #     if char not in count:
        #         return False

        #     count[char] -= 1

        #     if count[char] <0 :
        #         return False

        # return True