a = [10, 9, 2024, 23452, -43, 2, 341]

def selection_sort(arr):
    if arr[0]:
        for y in range(0, len(arr)-1):
            print(arr)
            min = arr[y]
            index = y
            for x in range(y, len(arr)):
                if arr[x] < min:
                    min = arr[x]
                    index = x
            holder = arr[y]
            arr[y] = min
            arr[index] = holder
        return arr
    else:
        return None

def bubble_sort(arr):
    has_swapped = True
    while has_swapped:
        has_swapped = False
        for index in range(0, len(arr)-1):
            if arr[index] > arr[index+1]:
                has_swapped = True
                holder = arr[index]
                arr[index] = arr[index+1]
                arr[index+1] = holder
                print(arr)
    return arr

print(a)
print(bubble_sort(a))
print(a)

# selection_sort(a)
# bubble_sort(a)