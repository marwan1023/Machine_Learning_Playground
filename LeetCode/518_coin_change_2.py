class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int

        beats 93.06%
        """
        coins.sort()
        dp = [1] + [0] * amount
        for c in coins:
            for i in range(c, amount+1):
                if dp[i-c]:
                    dp[i] += dp[i-c]
        return dp[-1]

    def change0(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int

        https://leetcode.com/problems/coin-change-2/discuss/99210/python-O(n)-space-dp-solution

        Because coins' order does not matter. For the first example, in your case, dp[3] will be 3, which are '2+1',
        '1+2', and '1+1+1'. It should be 2, which are '1+2' and '1+1+1'.

        beats 55.21%
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in coins:
            for j in range(1, amount + 1):
                if j >= i:
                    dp[j] += dp[j - i]
        return dp[amount]

    def change1(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int

        https://leetcode.com/problems/coin-change-2/discuss/99235/Classic-problem-python-clean-DP-O(MN)

        beats 34.72%
        """
        dp = [1] + [0] * amount
        for c in coins:
            for i in range(1, amount + 1):
                if i >= c:
                    dp[i] += dp[i - c]
        return dp[-1]

    def change2(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int

        TLE for test case: 500, [3,5,7,8,9,10,11]
        """
        if amount < 0:
            return 0
        if amount == 0:
            return 1
        if coins is None:
            return 0
        if len(coins) == 0:
            if amount == 0:
                return 1
            else:
                return 0

        coins.sort(reverse=True)
        if amount < coins[-1]:
            return 0
        res = [0]
        self.help_func(coins, amount, 0, res)
        return res[0]

    def help_func(self, coins, amount, depth, res):
        """
        :param coins:
        :param amount:
        :param depth:
        :param res_list:
        :return:

        use current largest coin as much as possible
        back tracking to use less largest coin if cannot make the target amount
        repeat above procedure for each coin from large to small
        """
        coins_len = len(coins)
        if amount == 0:
            res[0] += 1
            return
        elif amount < 0:
            return
        else:
            if depth == coins_len:
                return
            else:
                i = depth
                coin_nums = amount // coins[i]
                for cur_coin_num in range(coin_nums, -1, -1):
                    cur_amount = amount - coins[i] * cur_coin_num
                    self.help_func(coins, cur_amount, depth + 1, res)
