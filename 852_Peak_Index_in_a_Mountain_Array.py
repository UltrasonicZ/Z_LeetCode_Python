class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l, r = 0, len(A) - 1
        while l < r:
            mid = (l + r) // 2
            if A[mid] < A[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l


if __name__ == "__main__":
    sol = Solution()
    print(sol.peakIndexInMountainArray([0, 1, 0]))
    print(sol.peakIndexInMountainArray([0, 1, 2, 3, 0]))
    # print(sol.peakIndexInMountainArray("UDLR"))