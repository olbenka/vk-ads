def hash(s):
    hash_table = {}
    for char in s:
        if char in hash_table:
            hash_table[char] += 1
        else:
            hash_table[char] = 1
    return hash_table


n = int(input())
s = list(map(int, input().split()))
ht = hash(s)

avg = n // 2
isFind = False
for i in ht:
    if ht[i] > avg:
        isFind = True
        print(i)
        break

if not isFind:
    print(-1)
