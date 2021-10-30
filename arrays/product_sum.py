# Justin Ventura Amazon Prep

def productSum(arr):
	return _productSum(arr, depth=1)

# Time: O(n) only visits each number in
# the array once.

# Space: O(d) stack frames on recursion
# where d is deepest depth
def _productSum(arr, depth):
	if type(arr) is int:
		return arr
	
	total = 0
	for elem in arr:
		total += _productSum(elem, depth+1)
	return depth * total

if __name__ == '__main__':
    array=[5, 2, [7, -1], 3, [6, [-13, 8], 4]]
    result = productSum(array)
    print(result)
    assert result == 12
