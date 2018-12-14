class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        location = [-1, -1]
        count = 0
        index = -2
        for i in range(len(nums)):
            if nums[i] == target:
                if count == 0:
                    location[0] = i
                count += 1
                index = i
        if index != -2:
            location[1] = index
        return [location[0], location[1]]


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))
    print(sol.searchRange([0], 0))
