from heapq import *

INF = 1 << 60


class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int

        beats 77.69%
        """
        delay, current_queue = [INF] * (N + 1), [(0, K)]
        delay[K] = 0
        neighbor_list = [[] for _ in range(N + 1)]
        for t in times:
            neighbor_list[t[0]] += [(t[2], t[1])]
        while current_queue:
            current_node = heappop(current_queue)[1]
            for neighbor_cost in neighbor_list[current_node]:
                cost = neighbor_cost[0]
                neighbor = neighbor_cost[1]
                neighbor_delay = delay[current_node] + cost
                if neighbor_delay < delay[neighbor]:
                    delay[neighbor] = neighbor_delay
                    heappush(current_queue, (delay[neighbor], neighbor))
        return -(INF in delay[1:]) or max(delay[1:])
