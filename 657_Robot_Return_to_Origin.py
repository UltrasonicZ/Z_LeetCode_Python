class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # direction_dict = {"U": [0, 1],
        #                   "D": [0, -1],
        #                   "L": [-1, 0],
        #                   "R": [1, 0]}
        # start = [0, 0]
        # for i in range(len(moves)):
        #     for j in range(2):
        #         start[j] += direction_dict[moves[i]][j]
        # return start == [0, 0]
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')


if __name__ == "__main__":
    sol = Solution()
    print(sol.judgeCircle("UD"))
    print(sol.judgeCircle("LL"))
    print(sol.judgeCircle("UDLR"))