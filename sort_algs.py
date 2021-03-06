a = [10, 9, 2, -192950, 2024, 23452, -43, 2, 3451029, 341, -1024]
b = [1.3554635246, 1.35213475635241, 1.132412756435, 1.2345768574632, 1.1456787654, 1.56372434565342, 1.1234568763524, 1.23456787654, 1.43453476352, 1.0456746354]
c = [9, 2930241, 210, 1034, 1, 53]

# iterates through array and finds the min/max value
# at the end of iteration, swaps the min/max value to the end of the array
# decrements the array size, iterates through smaller array
# repeat until array size is 0
# very slow sort, low space requirements
def selection_sort(arr):
    # as long as there is a value in the array, run
    if arr[0]:
        # iterates once per length of array minus one, (last value does not need sorting E.g already placed)
        for y in range(0, len(arr)-1):
            print(arr)
            #min defaulted to 'first' value in array
            #array size decreases each loop as y increments
            min = arr[y]
            #tracks index of current min value
            index = y
            for x in range(y, len(arr)):
                if arr[x] < min:
                    min = arr[x]
                    index = x
            # swap 'first' element with lowest element found
            holder = arr[y]
            arr[y] = min
            arr[index] = holder
        return arr
    else:
        return None

# iterates through array two elements at a time, compares and if left is > right, swaps
# as a result, elements are carried up to the top by highest value, 'bubbleing up'
#requires one additional pass through with no swaps to confirm array is sorted
def bubble_sort(arr):
    has_swapped = True
    while has_swapped:
        # remains false if no swaps occur, breaking loop
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

# Goes through elements one-by-one, then reverses through the sorted portions of the array
# 'Inserts' elements where they belong in the order
# Does this by iterating backwards as long as the values are greater than the value to be inserted
# Moves all elements to the right along the way
# Upon reaching insertion condition, inserts last value
def insertion_sort(arr):
    #iterate through values one-by-one
    for i in range(1, len(arr)):
        print(arr)
        value = arr[i]
        # j can be 0 at the lowest
        j = i-1
        # loops as long as value to insert is less than the value on the backtrack
        while j >= 0 and value < arr[j]:
            # moves each value 'right'
            arr[j+1] = arr[j]
            j -= 1
        # once conditions are met, inserts value in appropriate slot
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

# Divide-and-conquer sort
# Recursively splits the array in hald until all arrays of length one
# Then, iterates through split arrays and constructs new array placing values in one-by-one
def merge_sort(arr):

    # recursively calls self with halves if arr length is greater than one
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = index = 0

        # takes left and right arrays, comparing values one-by-one
        # re-inserts them in place in origional array by index, increments index
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[index] = left[i]
                i+=1
            else:
                arr[index] = right[j]
                j+=1
            index+=1
        
        # Above loop breaks as soon as left or right reach their end
        # This means that there will be values remaining in the other array
        # These loops empty out the remaining values in either
        while i < len(left):
            arr[index] = left[i]
            i+=1
            index+=1
        
        while j < len(right):
            arr[index] = right[j]
            j+=1
            index+=1

        print(arr)
    
# TODO
def iterative_merge_sort(arr):
    return

# Selects a value to split the array by (this implementation uses the last value)
# Swaps all values less than the pivot to the left, greater than to the right
# Recursively calls self on each of the partitioned arrays
def quick_sort(arr, start, end):

    # Separates values to left and right of pivot (last value)
    def partition(arr, start, end):
        # pivot is last value in array based on end
        pivot = arr[end]
        i = start - 1

        # Iterate through elements of sub-array
        for j in range(start, end):
            # If element is less than pivot, swaps with value on left and increments that index (i)
            if arr[j] < pivot:
                i+=1
                holder = arr[j]
                arr[j] = arr[i]
                arr[i] = holder
        
        # last value will be the "middle" element
        arr[end] = arr[i+1]
        # "Middle" element is not pivot value
        arr[i+1] = pivot
        #return index of the pivot to produce new sub-arrays for recursion
        return i + 1

    # calls partition to organize array into lower and higher halves
    # then recursively calls quick_sort function with each flanking half
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
# Generates a binary heap (max heap here)
# Removes top (root) value
# Re-heaps until fully sorted
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

# counting sort first finds the max value in an array, then makes an array with a number of slots equal to that value
# It fills all indeces with 0's, then iterates through origional, incrementing by 1 at the index of the value
# It iterates through the counting array where every index is now the previous index plus it's origional value
# After this, the values in each counting array index represent there place in the sorted array
# We iterate through the origional array, go to the index of the value in the count array, based on the value of the count array at the target index, we place that value in the new "place", then decrement that indexes value by one.
# https://www.youtube.com/watch?v=7zuGmKfUt7s This video explains it very well with visual aid
# ALSO, this implementation does not work with positive values, if negatives are present in the array, adjustments need to be made using an
# adjuster value to properly represent the range of values in the array
def counting_sort(arr):
    # make an array with indeces for all values 0 - array max
    maxVal = max(arr)
    newArr = [0]*(maxVal+1)

    #for each value in array, increment the value at it's corresponding index by 1
    for i in range(0, len(arr)):
        newArr[arr[i]] += 1
    
    # iterate through count array and make all indeces equal to themselves plus the previous index
    for i in range(1, len(newArr)):
        newArr[i] += newArr[i-1]
    
    #new Array needed for as original must be intact to reference until re-filling is complete
    finalArr = [None]*len(arr)
    for i in range(0, len(arr)):
        # for each value in original array, the value ar it's corresponding index in the count array is it's 'place' in the final sorted array
        finalArr[newArr[arr[i]]-1] = arr[i]
        # Once placed, decrement the count array value by one
        newArr[arr[i]] -= 1

    # replace origional array values with sorted final array values
    for i in range(0, len(arr)):
        arr[i] = finalArr[i]

# Radix sort runs a counting sort several times one digit at a time, starting at the least significant digit(ones) up to the most significant
# Counting sort drops in performance compared to other sorting algs when the max value of an array approaches it's length^2
# Sorts properly even with negatives, but breaks if max value in array is not positive, needs adjusting
def radix_sort(arr):

    # runs the counting sort subroutine for radix, being passed a place value to isolate the digit
    def radix_count_sort_subroutine(arr, place):
        # new array of same length, count array will always be from 0 - 9
        n = len(arr)
        newArr = [0] * n
        count = [0] * 10

        for i in range(0, n):
            #get the index by dividing the number by it's place, then modulo 10 the resulting value. Will give an integer for the place you've represented
            index = (arr[i]/place)
            # increment the count array at the digit by one
            count[(index)%10] += 1
        
        # Same as count sort, sum values
        for i in range(1, 10):
            count[i] += count[i-1]
        
        # re-find value by getting array[i], then based on it's resulting place index, put that new pseudo-sorted value in the newArr just as in count sort
        i = n-1
        while i >= 0:
            index = (arr[i]/place)
            newArr[count[(index)%10]-1] = arr[i]
            count[(index)%10] -= 1
            i -= 1
        
        #fills origional array with newly sorted values
        i = 0
        for i in range(0, n):
            arr[i] = newArr[i]
    
    maxVal = max(arr)

    place = 1
    print(arr)
    # Repeatedly runs radix sort incrementing place value *10, until the max valeus most significant digit is reached
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

#below implementation uses bucket size of 0.1, expects values > 1, < 2
# bucket sort first divides values up into 'buckets' of value ranges, then runs insertion sort on each bucket, then concats the sorted arrays
# bucket sort works well when you have an even spread of values across your data
def bucket_sort(arr):
    # standard insertion sort
    def bucket_insert_sort_subroutine(arr):
        for i in range(1, len(arr)):
            value = arr[i]
            j = i-1
            while j >= 0 and arr[j] > value:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = value
        return arr
    
    bucketArr = []
    slot_num = 10

    # Fills bucket array with buckets
    for i in range(slot_num):
        bucketArr.append([]) # adds 'buckets' for each slot

    # Fills buckets based on their value range
    for j in arr:
        bucket_index = int(slot_num*j)%10
        bucketArr[bucket_index].append(j)

    # Sorts each bucket
    for i in range(slot_num):
        bucket_insert_sort_subroutine(bucketArr[i])
    
    # Updates original arr in place with sorted values
    k = 0
    for i in range(len(bucketArr)):
        for j in range(len(bucketArr[i])):
            arr[k] = bucketArr[i][j]
            k += 1

# Shell sort runs an insertion sort with gaps
# The idea is that in shell sort, some elements need to be moved far, requiring a lot of moves in insertion sort implementation
# shell sort starts with a gap value and moves the farther values closer to their sorted positions first
def shell_sort(arr):

    # initializes gap to half of arr length
    n = len(arr)
    gap = n//2


    while gap > 0:

        #Start with elements right of gap, iterate back, when encountering a value greater than element, swap two elements. Continue to next value
        for i in range(gap, n):
            holder = arr[i]

            j = i
            while j>=gap and arr[j-gap] > holder:
                arr[j] = arr[j-gap]
                j-= gap
            
            arr[j] = holder
        
        #halves gap until one, then zero
        gap //= 2
 
# selection_sort(a)
# bubble_sort(a)
# recursive_bubble_sort(a)
# insertion_sort(a)
# recursive_insertion_sort(a, len(a))
# merge_sort(a)
quick_sort(a, 0, len(a)-1)
# heap_sort(a, len(a), max(a))
# counting_sort(c)
# radix_sort(a)
# bucket_sort(b)
# shell_sort(a)

print(a)
# print(b)
# print(c)

#Fortwood Texas 