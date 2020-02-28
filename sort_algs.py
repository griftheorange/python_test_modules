a = [10, 9, 2, -192950, 2024, 23452, -43, 2, 3451029, 341, -1024]



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
        print(arr[start:end+1])
        pi = partition(arr, start, end)
        print(arr[start:end+1])
        quick_sort(arr, start, pi - 1)
        quick_sort(arr, pi + 1, end)

# TODO
def iterative_quick_sort(arr):
    return

# Heap sort reference below for visualizing
# Heap sort is much easier to understand with a mental image of what's going on
# https://www.youtube.com/watch?v=MtQL_ll5KhQ
def heap_sort(arr, n, max):

    def heapify(arr, n, i):
        print("Heaping from index {}".format(i))
        largest = i
        l = 2*i + 1
        r = 2*i + 2
    
        print(arr)
        # Comment in to track indices of left and right children for each run
        # print(i)
        # print(l)
        # print(r)
        if l < n and arr[l] > arr[largest]:
            largest = l
        
        if r < n and arr[r] > arr[largest]:
            largest = r
        
        if largest != i:
            # Comment in to see swaps in action
            # print("Swapping {} with {}".format(arr[i], arr[largest]))
            holder = arr[largest]
            arr[largest] = arr[i]
            arr[i] = holder
            heapify(arr, n, largest)

    # build heap
    print("Building Heap")
    for i in reversed(range(0, n/2)):
        heapify(arr, n, i)

    print("Reducing Heap, then re-building")
    # Extract Elems one by one
    for i in reversed(range(0, n)):
        holder = arr[0]
        arr[0] = arr[i]
        arr[i] = holder
        heapify(arr, i, 0)

    print("Final array")
    print(arr)

def counting_sort(arr):
    maxVal = max(arr)
    minVal = min(arr)
    adjuster = 0 - minVal
    newArr = [0]*(maxVal+1+adjuster)

    for i in range(0, len(arr)):
        newArr[arr[i]+adjuster] += 1
    
    for i in range(1, len(newArr)):
        newArr[i] += newArr[i-1]
    
    #new Array needed as original must be intact to reference until re-filling is complete
    finalArr = [None]*len(arr)
    for i in range(0, len(arr)):
        finalArr[newArr[arr[i]+adjuster]-1] = arr[i]
        newArr[arr[i]+adjuster] -= 1

    return finalArr

# Sorts properly even with negatives, but breaks if max value in array is not positive, needs adjusting
def radix_sort(arr):
    def radix_count_sort_subroutine(arr, place):
        n = len(arr)
        newArr = [0] * n
        count = [0] * 10

        for i in range(0, n):
            index = (arr[i]/place)
            count[(index)%10] += 1
        
        for i in range(1, 10):
            count[i] += count[i-1]
        
        i = n-1
        while i >= 0:
            index = (arr[i]/place)
            newArr[count[(index)%10]-1] = arr[i]
            count[(index)%10] -= 1
            i -= 1
        
        i = 0
        for i in range(0, n):
            arr[i] = newArr[i]
    
    maxVal = max(arr)

    place = 1
    print(arr)
    while maxVal/place > 0:
        radix_count_sort_subroutine(arr, place)
        print(arr)
        place *= 10
    
    # moves all negative values to the front of the array
    for i in range(0, len(arr)):
        if arr[i] < 0:
            negs = arr[i:]
            pos = arr[0:i]
            break
    if negs:
        index = 0
        for i in range(0, len(negs)):
            arr[index] = negs[i]
            index += 1
        for i in range(0, len(pos)):
            arr[index] = pos[i]
            index += 1



# selection_sort(a)
# bubble_sort(a)
# recursive_bubble_sort(a)
# insertion_sort(a)
# recursive_insertion_sort(a, len(a))
# merge_sort(a)
# quick_sort(a, 0, len(a)-1)
# heap_sort(a, len(a), max(a))
# counting_sort(a)
radix_sort(a)
print(a)


#Fortwood Texas 