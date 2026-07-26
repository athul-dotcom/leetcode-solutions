class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ""

        for ch in s:
            if ch.isalnum():
                text += ch.lower()

        return text == text[::-1]