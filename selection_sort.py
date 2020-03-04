def SelectionSort(arr):
    result=[]
    for i in range(len(arr)):
        smallest=arr[0]
     
        for x in arr:
            
            if x<smallest:
                smallest=x
                
        result.append(smallest)
        
        arr.remove(smallest)
    return result

a=[6, 5, 3, 1, 8, 7, 2, 4]
print(SelectionSort(a))
