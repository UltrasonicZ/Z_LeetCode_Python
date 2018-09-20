class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack_s = [None]
        dict_s = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in dict_s:
                if dict_s[c] != stack_s.pop():
                    return False
            else:
                stack_s.append(c)
        return len(stack_s) == 1
        # pars = [None]
        # parmap = {')': '(', '}': '{', ']': '['}
        # for c in s:
        #     if c in parmap:
        #         if parmap[c] != pars.pop():
        #             return False
        #     else:
        #         pars.append(c)
        # return len(pars) == 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("["))
    # print(sol.isValid("()[]{}"))
    # print(sol.isValid("(]"))
    # print(sol.isValid("([)]"))
    # print(sol.isValid("{[]}"))
    # print(sol.isValid("hello world"))