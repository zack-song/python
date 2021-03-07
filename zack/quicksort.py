def quicksort(arr,low,higth):
    pivot = arr[low]
    i = low
    j = higth
    while i < j:
        while i<j and arr[j] >= pivot:
            j -= 1
        if i<j:
            arr[i] = arr[j]
        while i<j and arr[i] <= pivot:
            i += 1
        if i<j:
            arr[j] = arr[i]
    arr[i] = pivot
    if low < higth:
        quicksort(arr,low,i-1)
        quicksort(arr,i+1,higth)






arr = [49,38,65,97,76,13,27,49]
quicksort(arr,0,len(arr)-1)
print(arr)
