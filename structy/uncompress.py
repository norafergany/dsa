def uncompress(s):
    result = []

    num = 0
    nums = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

    i = 0
    j = 0

    while j < len(s):
        if s[j] not in nums:
            num = int(s[i:j])
            ch = s[j]
            result.extend([ch for x in range(num)])
            j += 1
            i = j
        else:
            j += 1
    return ("".join(result))

# Time: O(n*m)
# Space O(n*m)
