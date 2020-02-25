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

def recursive_bubble_sort(arr):
    print(arr)
    for i, num in enumerate(arr):
        # iterates through each index of array
        try:
            if arr[i+1] < num:
                # on encounter of first 'unsorted' pair, swaps values then re-calls the function, starting back from beginning
                arr[i] = arr[i+1]
                arr[i+1] = num
                recursive_bubble_sort(arr)
        except IndexError:
            # base case
            # if the algorithm reaches the end of the array, arr[i+1] throws IndexError
            # catches and passes, code reaches return statement
            pass
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        print(arr)
        value = arr[i]
        j = i-1
        while j >= 0 and value < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = value
    return arr



# print(a)
# print(insertion_sort(a))
# print(a)

# selection_sort(a)
# bubble_sort(a)
# recursive_bubble_sort(a)
# insertion_sort(a)