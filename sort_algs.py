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

def recursive_insertion_sort(arr, n):
    if (n <= 1):
        return
   
    recursive_insertion_sort(arr, n-1)
    
    last = arr[n-1]
    j = n-2

    while (j>=0 and arr[j]>last):
        arr[j+1] = arr[j]
        j = j - 1
    arr[j+1]=last
    print(arr)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1

        print(arr)
    
# TODO
def iterative_merge_sort(arr):
    return

def quick_sort(arr, start, end):

    def partition(arr, start, end):
        pivot = arr[end]
        i = start - 1

        for j in range(start, end):
            if arr[j] < pivot:
                i+=1
                holder = arr[j]
                arr[j] = arr[i]
                arr[i] = holder
        
        arr[end] = arr[i+1]
        arr[i+1] = pivot
        return i + 1

    if start < end:
        print arr[start:end+1]
        pi = partition(arr, start, end)
        print arr[start:end+1]
        quick_sort(arr, start, pi - 1)
        quick_sort(arr, pi + 1, end)

# TODO
def iterative_quick_sort(arr):
    return

# print(a)
# print(recursive_insertion_sort(a))
# print(a)

# selection_sort(a)
# bubble_sort(a)
# recursive_bubble_sort(a)
# insertion_sort(a)
# recursive_insertion_sort(a, len(a))
# merge_sort(a)
quick_sort(a, 0, len(a)-1)