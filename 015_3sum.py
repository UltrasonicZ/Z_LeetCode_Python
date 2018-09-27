class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        list_a = []
        nums_cp = sorted(nums)
        for i in range(len(nums) - 2):
            if i > 0 and nums_cp[i] == nums_cp[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums_cp[i] + nums_cp[j] + nums_cp[k] < 0:
                    j += 1
                    # while nums_cp[j] == nums_cp[j - 1] and j < k:
                    #     j += 1
                elif nums_cp[i] + nums_cp[j] + nums_cp[k] > 0:
                    k -= 1
                    # while nums_cp[k] == nums_cp[k + 1] and j < k:
                    #     k -= 1
                else:
                    list_a.append([nums_cp[i], nums_cp[j], nums_cp[k]])
                    j += 1
                    k -= 1
                    while nums_cp[j] == nums_cp[j - 1] and j < k:
                        j += 1
                    while nums_cp[k] == nums_cp[k + 1] and j < k:
                        k -= 1
        return list_a


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
    print(sol.threeSum([-2, 0, 0, 2, 2]))
    print(sol.threeSum([0, 0, 0]))
    # print(sol.threeSum([7, -13, -1, 1, -6, 14, 10, -2, 1, 9, 11, -10, 8, -10, 14, 13, -1, 4, -6, -3, -5, 3, 3, 12, -5, 11, 5, -6, -2, 0,
    #  -6, 12, 3, 0, -2, 12, -1, -7, -5, 8, 10, 13, 13, 3, 10, 12, -7, -6, -7, -5, -1, 3, 5, -13, -8, -15, 13, 13, -14,
    #  -12, -2, -5, -15, 8, 11, -1, 6, -13, -1, 8, 10, -14, -1, 0, -4, -6, -3, 5, -4, -2, 7, 10, 8, -3, 12, -14, -10, 3,
    #  14, -9, -2, -11, -6, -9, 13, 12, -3, 4, 14, 3, -11, 2, 5, -5, -13, -14, -3, -8]))