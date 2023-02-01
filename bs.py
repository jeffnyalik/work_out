def binarySearch(arr, l, r, key):
    if l > r:
        return -1
    else:
        middle = (l + r)//2
        if key == arr[middle]:
            return middle
        elif key < arr[middle]:
            return binarySearch(arr, l, middle - 1, key)
        else:
            return binarySearch(arr, middle + 1, r, key)


arr = [2, 5, 6, 8, 9, 10]
key = 100
index = binarySearch(arr, 0, len(arr)-1, key)
if(index != -1):
    print(index)
else:
    print("Does not exist")