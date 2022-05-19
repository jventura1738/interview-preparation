# Justin Ventura

# Length of Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s: str) -> int:
    seen = set()
    length = 0
    l = 0
    for r in range(len(s)):
        current = s[r]
        while current in seen:
            seen.remove(s[l])
            l += 1
        seen.add(current)
        length = max(length, len(seen))

    return length


if __name__ == '__main__':
    # Write tests for lengthOfLongestSubstring here.
    assert lengthOfLongestSubstring('abcabcbb') == 3
    assert lengthOfLongestSubstring('bbbbb') == 1
    assert lengthOfLongestSubstring('pwwkew') == 3
