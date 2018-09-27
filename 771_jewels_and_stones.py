class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for i in range(len(J)):
            for j in range(len(S)):
                if S[j] == J[i]:
                    count += 1
        return count

        # return sum(s in J for s in S)


if __name__ == "__main__":
    sol = Solution()
    print(sol.numJewelsInStones("aA", "aAAbbbb"))
    print(sol.numJewelsInStones("z", "ZZ"))
    # print(sol.numJewelsInStones("LOVELY"))