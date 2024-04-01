def longest_increasing_subsequence(nums):
    result = 0

    for x in range(len(nums)):
        sub_seq = []
        curr = nums[x]
        sub_seq.append(curr)
        for y in range(x + 1, len(nums) - 1):

            if nums[y] > curr:
                curr = nums[y]
                sub_seq.append(curr)
        if len(sub_seq) > result:
            result = len(sub_seq)

    return result