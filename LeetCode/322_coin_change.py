class Solution(object):
    """
    This solution is inspired by the BFS solution for problem Perfect Square.
    Since it is to find the least coin solution (like a shortest path from 0 to amount),
    using BFS gives results much faster than DP.
    https://discuss.leetcode.com/topic/26262/short-python-solution-using-bfs

    beats 97.75%
    """
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        value1 = [0]
        value2 = []
        nc = 0
        visited = [False] * (amount + 1)
        visited[0] = True
        while value1:
            nc += 1
            for v in value1:
                for coin in coins:
                    new_val = v + coin
                    if new_val == amount:
                        return nc
                    elif new_val > amount:
                        continue
                    elif not visited[new_val]:
                        visited[new_val] = True
                        value2.append(new_val)
            value1, value2 = value2, []
        return -1
