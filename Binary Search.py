def binary_search(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

# Example usage
arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)
print("Element is present at index", result)  # Output: Element is present at index 3
