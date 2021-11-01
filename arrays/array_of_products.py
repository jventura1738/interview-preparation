# Justin Ventura

# O(n) SPACE TIME
def arrayOfProducts(arr):
    left_prod = [1]*len(arr)
    current_product = 1
    for i in range(len(arr)):
	    left_prod[i] = current_product
	    current_product *= arr[i]
    current_product = 1
    for i in range(len(arr)-1, -1, -1):
        left_prod[i] *= current_product
        current_product *= arr[i]
    return left_prod


if __name__ == '__main__':
    test=[5, 1, 4, 2]
    result=arrayOfProducts(test)
    print(result)
    assert result == [8, 40, 10, 20]
