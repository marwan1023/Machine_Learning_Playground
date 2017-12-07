class Solution(object):
    # @return an integer
    # beats 86.09%
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = max_length = 0
        used_char = {}

        for i in range(len(s)):
            if s[i] in used_char and start <= used_char[s[i]]:
                start = used_char[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used_char[s[i]] = i

        return max_length
