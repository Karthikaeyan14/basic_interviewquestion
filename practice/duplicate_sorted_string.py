def removeDuplicates(arr):
    n = len(arr)
    if n <= 1:
        return n

    # Start from the second element
    idx = 1

    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            arr[idx] = arr[i]
            idx += 1

    return idx


arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
newSize = removeDuplicates(arr)

for i in range(newSize):
    print(arr[i], end=" ")