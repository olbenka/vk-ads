s = input()
stack = []

for i in s:
    if not stack:
        stack.append(i)
        continue

    if stack[len(stack)-1] == i:
        stack.pop(len(stack) - 1)
    else:
        stack.append(i)

res = ''
for i in stack:
    res += i
print(res)
