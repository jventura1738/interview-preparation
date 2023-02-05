# Justin Ventura

"""

Given a word, return the next largest word that can be made with the same letters.
The word need not exist in the dictionary.  If this word is already the last
possible word permutation, return the string "no answer"

Example:
    for "cat" -> "cta"
    for "dog" -> "dgo"
    for "aaa" -> "aaa"
    for "zyx" -> "no answer"

This is my solution for JP Morgan.
"""

# O(n) TIME
def next_largest_word(word):
    chars = list(word)
    i = len(chars) - 1    
    while i > 0:
        if chars[i - 1] < chars[i]:
            break
        i -= 1
    # This means we must be at the last permutation.
    else:
        return "no answer"

    j = len(chars) - 1
    while chars[j] <= chars[i - 1]:
        j -= 1
    # Swap the chars when we find the next largest.
    chars[i - 1], chars[j] = chars[j], chars[i - 1]

    # Reverse after i.
    chars[i:] = chars[len(chars)-1:i-1:-1]
    return ''.join(chars)


# Tests:
if __name__ == '__main__':
    test = "cat"
    result = next_largest_word(test)
    print(result)
    assert result == "cta"

    test = "dog"
    result = next_largest_word(test)
    print(result)
    assert result == "gdo"

    test = "zyx"
    result = next_largest_word(test)
    print(result)
    assert result == "no answer"

    test = "dkhc"
    result = next_largest_word(test)
    print(result)
    assert result == "hcdk"

    test = "yx"
    result = next_largest_word(test)
    print(result)
    assert result == "no answer"

    test = "xy"
    result = next_largest_word(test)
    print(result)
    assert result == "yx"

    test = "hefg"
    result = next_largest_word(test)
    print(result)
    assert result == "hegf"

    test = "abdc"
    result = next_largest_word(test)
    print(result)
    assert result == "acbd"

    test = "fedcbabcd"
    result = next_largest_word(test)
    print(result)
    assert result == "fedcbabdc"
