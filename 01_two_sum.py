def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            a = target - nums[i]
            b = nums[j]
            if a != b:
                continue
            else:
                return [i, j]


if __name__ == "__main__":
    nums_in = input()
    target = int(input())
    numbers = nums_in.split()
    # print(numbers)
    nums = [0] * len(numbers)
    for i in range(len(numbers)):
        nums[i] = int(numbers[i])
    print(twoSum(nums, target))
