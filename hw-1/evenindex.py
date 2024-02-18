n = int(input())
arr = list(map(int, input().split()))

even_index = 0

for i in range(n):
    if arr[i] % 2 == 0:
        arr[i], arr[even_index] = arr[even_index], arr[i]
        even_index += 1

print(*arr)
