a = [10, 9, 2024, 23452, -43, 2, 341]

def selection_sort(arr):
    if arr[0]:
        newArr = []
        for y in range(0, len(arr)-1):
            min = arr[0]
            index = 0
            for x in range(y, len(arr)):
                if arr[x] < min:
                    min = arr[x]
                    index = x
            s1 = slice(0, index)
            s2 = slice(index+1, len(arr))
            newArr.append(arr[index])
            arr = arr[s1] + arr[s2]
        return newArr
    else:
        return None

meh