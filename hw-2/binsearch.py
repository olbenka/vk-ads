def binSearch(arr, num):
    l = 0
    r = len(arr)

    if r==0 or num<arr[0] or num> arr[-1]:
        return -1

    while l <= r:
        mid = (l+r)//2
        if (num == arr[mid]):
            return mid
        if (num < arr[mid]):
            r = mid-1
        else:
            l = mid+1

    return -1

n = int(input())
arr = list(map(int, input().split()))
num = int(input())
tmp = binSearch(arr, num)
if tmp == -1:
    print('false')
else:
    print('true')


