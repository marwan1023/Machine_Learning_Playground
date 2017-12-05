import collections

class Solution(object):
    # beats 24.97%
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s, t = sorted(s), sorted(t)
        return t[-1] if s == t[:-1] else [x[1] for x in zip(s, t) if x[0] != x[1]][0]

    # beats 96.00%
    def findTheDifference1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return chr(reduce(operator.xor, map(ord, s + t)))

    # beats 31.10%
    def findTheDifference2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return list((collections.Counter(t) - collections.Counter(s)))[0]