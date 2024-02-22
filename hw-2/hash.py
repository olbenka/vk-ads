def hash_string(s):
    hash_table = {}
    for char in s:
        if char in hash_table:
            hash_table[char] += 1
        else:
            hash_table[char] = 1
    return hash_table


def is_anagram(a, b):
    hash_a = hash_string(a)
    hash_b = hash_string(b)

    return hash_a == hash_b


s = input().split()
a = s[0]
b = s[1]

if is_anagram(a,b):
    print('true')
else:
    print('false')
