def max_cyclic_sum(s):
    n = len(s)
    s = s + s
    char_set = set()

    left = 0
    curr_sum = 0
    max_sum = 0

    for right in range(len(s)):
        while s[right] in char_set or (right - left + 1) > n:
            char_set.remove(s[left])
            curr_sum -= (ord(s[left]) - ord('a') + 1)
            left += 1

        char_set.add(s[right])
        curr_sum += (ord(s[right]) - ord('a') + 1)

        max_sum = max(max_sum, curr_sum)

    return max_sum


if __name__ == "__main__":
    s = input().strip()
    print(max_cyclic_sum(s))
