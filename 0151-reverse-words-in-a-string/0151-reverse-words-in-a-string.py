class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        wordssort = reversed(words)
        wordssorted = " ".join(wordssort)
        return wordssorted