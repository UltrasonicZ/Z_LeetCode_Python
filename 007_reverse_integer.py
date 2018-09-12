def reverse(x):
    list_a = list(str(x))
    # list_b = []
    x_num = x
    num = 0
    if x_num >= 0 and x_num <= 2**31-1:
        while list_a:
            num = num*10 + int(list_a.pop(-1))
            if num > 2 ** 31-1:
                num = 0
        return num
    elif x_num < 0 and x_num >= -2**31:
        del list_a[0]
        while list_a:
            num = num*10 + int(list_a.pop(-1))
            if num > 2 ** 31:
                num = 0
        return -num
    else:
        return 0


if __name__ == "__main__":
    while True:
        x = input()
        x = int(x)
        print(reverse(x))
        print(2**31)
