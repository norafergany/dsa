def compress(s):
    """
    use 2 points
    initialize char as first char
    keep iterating until you find a char thats different
    count the chars and add the number and char to the string

    """
    i = 0
    j = 0

    result = []
    while j < len(s):
        curr_ch = s[i]

        if s[j] == s[i]:
            j += 1

        else:
            num = j - i
            if num != 1:
                result.append(str(num))
            result.append(curr_ch)
            i = j

    num = j - i
    if num != 1:
        result.append(str(num))
    result.append(curr_ch)

    return "".join(result)

# Time: O(n + [digits]*number of groups)
# Space: O(2*number of groups)
