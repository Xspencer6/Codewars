def count(s):
    # The function code should be here
    ans = {}
    for char in s:
        if char in ans:
            ans[char] += 1
        else:
            ans[char] = 1
    return ans
