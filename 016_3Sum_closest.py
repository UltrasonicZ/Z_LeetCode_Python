class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums_cp = sorted(nums)
        sum_ijk = float("inf")
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if (sum_ijk - target) ** 2 > (nums_cp[i] + nums_cp[j] + nums_cp[k] - target) ** 2:
                    sum_ijk = nums_cp[i] + nums_cp[j] + nums_cp[k]
                if nums_cp[i] + nums_cp[j] + nums_cp[k] < target:
                    j += 1
                elif nums_cp[i] + nums_cp[j] + nums_cp[k] > target:
                    k -= 1
                else:
                    return target
        return sum_ijk


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSumClosest([-1, 0, 1, 2, -1, -4], 1))
    print(sol.threeSumClosest([-5, 1, 4], 2))
    print(sol.threeSumClosest([-1, 2, 1, -4], 1))
    print(sol.threeSumClosest([1, 1, 1, 0], -100))
    print(sol.threeSumClosest([1, 2, 4, 8, 16, 32, 64, 128], 82))
