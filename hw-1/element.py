n = int(input())
arr = list(map(int, input().split()))
element = int(input())

count = 0
for i in range(n):
    if arr[i] != element:
        count += 1

print(count)
