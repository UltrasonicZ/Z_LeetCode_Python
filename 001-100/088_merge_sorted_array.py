class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1_cp = nums1.copy()
        i = 0
        j = 0
        k = 0
        while j < m and k < n:
            if nums1_cp[j] < nums2[k]:
                nums1[i] = nums1_cp[j]
                i += 1
                j += 1
            else:
                nums1[i] = nums2[k]
                i += 1
                k += 1
        for a in range(j, m):
            nums1[i] = nums1_cp[a]
            i += 1
        for b in range(k, n):
            nums1[i] = nums2[b]
            i += 1
        return nums1

        # nums1_cp = nums1.copy()
        # i = 0
        # j = 0
        # k = 0
        # while j < m and k < n:
        #     if nums1_cp[j] < nums2[k]:
        #         nums1[i] = nums1_cp[j]
        #         i += 1
        #         j += 1
        #     else:
        #         nums1[i] = nums2[k]
        #         i += 1
        #         k += 1
        # if j < m:
        #     tmp = j
        #     for i in range(j + k, m + n):
        #         nums1[i] = nums1_cp[tmp]
        #         tmp += 1
        # if k < n:
        #     tmp = k
        #     for i in range(j + k, n + m):
        #         nums1[i] = nums2[tmp]
        #         tmp += 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
