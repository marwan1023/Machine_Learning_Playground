class Solution(object):
    # beats 62.23%
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        The smaller numbers on the right of a number are exactly those that jump from its right to its left during a
        stable sort. So I do merge sort with added tracking of those right-to-left jumps.
        """
        def sort(enum):
            half = len(enum) / 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])  # merge sort left and right parts
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:  # have smaller one in right
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller

    def countSmaller1(self, nums):
        def sort(enum):
            half = len(enum) / 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                m, n = len(left), len(right)
                i = j = 0
                while i < m or j < n:
                    if j == n or i < m and left[i][1] <= right[j][1]:
                        enum[i + j] = left[i]
                        smaller[left[i][0]] += j
                        i += 1
                    else:
                        enum[i + j] = right[j]
                        j += 1
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller

    def countSmaller2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        solution with Segment Tree

        beats 2.58%
        """
        hash_table = {v: i for i, v in enumerate(sorted(set(nums)))}

        tree, r = SegmentTree(len(hash_table)), []
        for i in xrange(len(nums) - 1, -1, -1):
            r.append(tree.sum(0, hash_table[nums[i]] - 1))
            tree.update(hash_table[nums[i]], 1)
        return r[::-1]

    def countSmaller3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        solution with Binary Index Tree

        beats 93.87%
        """
        hash_table = {v: i for i, v in enumerate(sorted(set(nums)))}

        tree, r = BinaryIndexedTree(len(hash_table)), []
        for i in xrange(len(nums) - 1, -1, -1):
            r.append(tree.sum(hash_table[nums[i]]))
            tree.update(hash_table[nums[i]] + 1, 1)
        return r[::-1]


class BinaryIndexedTree(object):
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def update(self, i, val):
        while i < len(self.sums):
            self.sums[i] += 1
            i += i & -i

    def sum(self, i):
        r = 0
        while i > 0:
            r += self.sums[i]
            i -= i & -i
        return r


class SegmentTreeNode(object):
    def __init__(self, val, start, end):
        self.val = val
        self.start = start
        self.end = end
        self.children = []


class SegmentTree(object):
    def __init__(self, n):
        self.root = self.build(0, n - 1)

    def build(self, start, end):
        if start > end:
            return

        root = SegmentTreeNode(0, start, end)
        if start == end:
            return root

        mid = start + end >> 1
        root.children = filter(None, [
            self.build(start, end)
            for start, end in ((start, mid), (mid + 1, end))])
        return root

    def update(self, i, val, root=None):
        root = root or self.root
        if i < root.start or i > root.end:
            return root.val

        if i == root.start == root.end:
            root.val += val
            return root.val

        root.val = sum([self.update(i, val, c) for c in root.children])
        return root.val

    def sum(self, start, end, root=None):
        root = root or self.root
        if end < root.start or start > root.end:
            return 0

        if start <= root.start and end >= root.end:
            return root.val

        return sum([self.sum(start, end, c) for c in root.children])