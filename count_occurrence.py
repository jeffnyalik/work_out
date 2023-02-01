"""Count occurence of a value"""

## Using Binary Search method
def binarySearch(arr, l, r, key):
    if l > r:
        return -1
    
    middle = (l + r) // 2
    if key == arr[middle]:
        return middle
    if key < arr[middle]:
        return binarySearch(arr, l, middle - 1, key)
    else:
        return binarySearch(arr, middle + 1, r, key)

def countOccurrence(arr, key):
    indexVal = binarySearch(arr, 0, len(arr)-1, key)
    if indexVal == -1:
        return 0

    count  = 1
    
    #count value on the left
    left = indexVal - 1
    while left >=0 and arr[left] == key:
        count +=1
        left -=1
    
    #count value on the right
    right = indexVal + 1
    while right < len(arr) and arr[right] == key:
        count+=1
        right+=1
    
    return count




"""def countOccurence(arr, key):
    if not arr:
        return []
    count = 0
    for i in range(len(arr)):
        if arr[i] == key:
            count +=1
    return count"""

arr = [ 1, 2, 2, 2, 2,
        3, 4, 7, 8, 8 ]
key = 2

print(countOccurrence(arr, key))