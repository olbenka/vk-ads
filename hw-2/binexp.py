def expSearch(arr, n, x):
    if(arr[0] == x):
        return 0,0

    i = 1
    while i < n and arr[i] <= x:
        i *= 2

    low = i//2
    high = min(i, n-1)

    return binSearch(arr, low, high, x)

def binSearch(arr, low, high, x):
    while low <= high:
        mid = (low+high)//2

        if arr[mid] == x:
            return low, high

        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1, -1

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

low, high = expSearch(arr, n, x)

print(low, high)
