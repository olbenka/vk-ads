def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][2] < right_half[j][2] or (left_half[i][2] == right_half[j][2] and left_half[i][1] < right_half[j][1]):
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


n = int(input())
books = []
for i in range(n):
    isbn, title, year = input().split('"')
    year = int(year.strip())
    books.append((isbn.strip(), title.strip(), year))

merge_sort(books)

for book in books:
    print(f'{book[0]} "{book[1]}" {book[2]}')
