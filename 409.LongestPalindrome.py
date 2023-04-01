class Solution:
    def longestPalindrome(self, s: str) -> int:
        frequency = {}
        len_ = 0

        for letter in s:
            frequency[letter] = frequency.get(letter, 0) + 1
        
        for i in frequency.values():
            if i % 2 == 0:
                len_ += i
            else:
                len_ += i - 1
                oddCount = True
        
        if oddCount:
            len_ += 1
        
        return len_