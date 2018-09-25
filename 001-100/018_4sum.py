class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        list_a = []
        nums_cp = sorted(nums)
        if len(nums_cp) == 4:
            if nums_cp[0] + nums_cp[1] + nums_cp[2] + nums_cp[3] == target:
                return [nums_cp]
            else:
                return []
        for i in range(len(nums)-3):
            if nums_cp[i] == nums_cp[i - 1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j == i + 1:
                    pass
                elif nums_cp[j] == nums_cp[j - 1]:
                    continue
                k = j + 1
                l = len(nums) - 1
                while j < k and k < l:
                    if nums_cp[i] + nums_cp[j] + nums_cp[k] + nums_cp[l] > target:
                        if nums_cp[l] == nums_cp[l - 1]:
                            l -= 1
                            continue
                        l -= 1
                    elif nums_cp[i] + nums_cp[j] + nums_cp[k] + nums_cp[l] < target:
                        if nums_cp[k] == nums_cp[k + 1]:
                            k += 1
                            continue
                        k += 1
                    else:
                        if [nums_cp[i], nums_cp[j], nums_cp[k], nums_cp[l]] not in list_a:
                            list_a.append([nums_cp[i], nums_cp[j], nums_cp[k], nums_cp[l]])
                        l -= 1
                        k += 1
        return list_a


if __name__ == "__main__":
    sol = Solution()
    print(sol.fourSum([1, 0, -1, 0, -2, 2], 0))
    print(sol.fourSum([-1,0,1,2,-1,-4], -1))
    print(sol.fourSum([-3,-2,-1,0,0,1,2,3], 0))
    print(sol.fourSum([0, 0, 0, 0], 1))
    print(sol.fourSum([-1, 0, -5, -2, -2, -2, -4, 0, 1, -2], -9))