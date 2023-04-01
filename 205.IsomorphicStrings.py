class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictS, dictT = {}, {}

        for i in range(len(s)):
            char1, char2 = s[i], t[i]
            
            if ((char1 in dictS and dictS[char1] != char2) or 
                (char2 in dictT and dictT[char2] != char1)):
                return False

            dictS[char1] = char2
            dictT[char2] = char1

        return True