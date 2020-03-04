def insertion_sort(arr):
    for j in range(1,len(arr)):
        key=arr[j]
        i=j-1
        for i in range(j-1,-1,-1):
            if i>=0 and arr[i]>key:

                arr[i+1]=arr[i]
                i=i-1
                arr[i+1]=key
    return arr
a=[6, 5, 3, 1, 8, 7, 2, 4,9,9]
print(insertion_sort(a))