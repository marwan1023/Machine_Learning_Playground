class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int

        O(m*n) space
        beats 54.30%
        """
        l1, l2 = len(word1) + 1, len(word2) + 1
        dp = [[0 for _ in range(l2)] for _ in range(l1)]
        for i in range(l1):
            dp[i][0] = i
        for j in range(l2):
            dp[0][j] = j
        for i in range(1, l1):
            for j in range(1, l2):
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (word1[i - 1] != word2[j - 1]))
        return dp[-1][-1]

    def minDistance1(self, word1, word2):
        """
        :param word1:
        :param word2:
        :return:

        O(n) space with rolling array
        beats 87.02%
        """
        l1, l2 = len(word1) + 1, len(word2) + 1
        pre = [0 for _ in range(l2)]
        for j in range(l2):
            pre[j] = j
        for i in range(1, l1):
            cur = [i] * l2
            for j in range(1, l2):
                cur[j] = min(cur[j - 1] + 1, pre[j] + 1, pre[j - 1] + (word1[i - 1] != word2[j - 1]))
            pre = cur[:]
        return pre[-1]
