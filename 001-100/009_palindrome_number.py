def isPalindrome(x):
    x = list(str(x))
    # half = int(len(x) / 2)
    # for i in range(half):
    #     if x[i] == x[-i - 1]:
    #         continue
    #     else:
    #         return False
    # return True

    x_orig = x.copy()
    x.reverse()
    if x_orig == x:
        return True
    else:
        return False


if __name__ == "__main__":
    while True:
        x = input()
        x = int(x)
        print(isPalindrome(x))