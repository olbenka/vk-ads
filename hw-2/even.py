n = int(input())
arr = list(map(int, input().split()))

stack = []
for i in range(n):
    elem = arr[i]
    if elem % 2 == 0:
        stack.append(elem)

if stack:
    print(stack[-1])
else:
    print(-1)
