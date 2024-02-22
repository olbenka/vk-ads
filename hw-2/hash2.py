def hash_string(s):
    hash_table = {}
    for char in s:
        if char in hash_table:
            hash_table[char] += 1
        else:
            hash_table[char] = 1
    return hash_table


s = input()
ht = hash_string(s)

maxim = 0
for i in ht:
    
    if ht[i] > maxim:
        maxim = ht[i]

print(maxim)

