# Justin Ventura Amazon Prep

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
	# Edge cases:
    if not len(redShirtSpeeds) or not len(blueShirtSpeeds):
        return 0
	
    # Sorting: O(nlogn)
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=fastest)
    total_speed = 0

    # Navigate the arrays O(n)
    for r, b in zip(redShirtSpeeds, blueShirtSpeeds):
        total_speed += max(r,b)

    return total_speed

if __name__ == '__main__':
    red=[5, 5, 3, 9, 2]
    blue=[3, 6, 7, 2, 1]
    result = tandemBicycle(red, blue, True)
    assert result == 32
    print(result)
