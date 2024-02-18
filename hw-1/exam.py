n = int(input())
arr = list(map(int, input().split()))
tmp = []
count = 0
for i in range(n):
    if arr[i] == 0:
        count += 1
    else:
        tmp.append(arr[i])

for i in range(count):
    tmp.append(0)

print(*tmp)
