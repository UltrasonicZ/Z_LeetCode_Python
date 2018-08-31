class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        self.nums1 = nums1
        self.nums2 = nums2
        nums3 = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        if i <= len(nums1):
            for i in range(i, len(nums1)):
                nums3.append(nums1[i])
        if j <= len(nums2):
            for j in range(j, len(nums2)):
                nums3.append(nums2[j])
        if len(nums3) % 2 == 1:
            return nums3[int(len(nums3)/2)]
        else:
            return nums3[int(len(nums3)/2)] / 2 + nums3[int(len(nums3)/2)-1] / 2


if __name__ == "__main__":

    sol = Solution()
    print(sol.findMedianSortedArrays([1, 2, 4, 7], [3, 5, 6]))

    print(sol.findMedianSortedArrays([1, 3], [2]))

    print(sol.findMedianSortedArrays([1, 2], [3, 4]))

