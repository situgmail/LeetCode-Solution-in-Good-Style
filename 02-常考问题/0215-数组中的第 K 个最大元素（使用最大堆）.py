import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums = [-_ for _ in nums]
        # 默认是最小堆
        heapq.heapify(nums)
        for _ in range(k):
            res = heapq.heappop(nums)
        return -res


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    solution = Solution()
    result = solution.findKthLargest(nums, k)
    print(result)
