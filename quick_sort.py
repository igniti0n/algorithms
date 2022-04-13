# Worst case is time: 0(n*n), but avarage is 0(n*log(n)).
# Worst time si when array is for ex [4, 3, 2, 1], so you are left with subbary of 1 each itteratioin
# Space is 0(log(n)), if you call the smaller subarray first, so it goes of the call sstack
# If yo dont, you can in worst case have linear space complexity

def quickSort(array):
    arrayLength = len(array)
    doQuicksort(array, 0, arrayLength - 1)
    return array

def doQuicksort(array, firstIndex, lastIndex):
    if firstIndex >= lastIndex:
        return
    pivot = firstIndex
    left = firstIndex + 1
    right = lastIndex
    while left <= right:
        if array[left] > array[pivot] and array[right] < array[pivot]:
            swap(array, left, right)
        if array[left] <= array[pivot]:
            left += 1
        if array[right] >= array[pivot]:
            right -= 1
    swap(array, right, pivot)
    #checks bcs of recursionn stack, so that in case for ex all right subarrays have 1 element
	#it first gets rid of that call, and then to the big one
    leftArraySmaller = right -1 - firstIndex < lastIndex - (right + 1)
    if leftArraySmaller:
        doQuicksort(array, firstIndex, right -1)
        doQuicksort(array, right + 1, lastIndex)
    else:
        doQuicksort(array, right + 1, lastIndex)
        doQuicksort(array, firstIndex, right -1)


def swap(array, a, b):
    array[a], array[b] = array[b], array[a]
