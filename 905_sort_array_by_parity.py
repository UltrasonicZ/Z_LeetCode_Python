class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # odd = []
        # even = []
        # for i in range(len(A)):
        #     if A[i] % 2 == 0:
        #         even.append(A[i])
        #     if A[i] % 2:
        #         odd.append(A[i])
        # even.extend(odd)
        # return even
        
        start, end = 0, len(A) - 1
        while start < end:
            m, n = A[start], A[end]
            if m % 2 == 1 and n % 2 == 0:
                A[start], A[end] = n, m
            elif m % 2 == 1:
                end -= 1
            elif n % 2 == 0:
                start += 1
            else:
                start += 1
                end -= 1
        return A


if __name__ == "__main__":
    sol = Solution()
    print(sol.sortArrayByParity([1, 1, 1, 2, 4]))
    # print(sol.sortArrayByParity("I"))
    # print(sol.sortArrayByParity("DI"))