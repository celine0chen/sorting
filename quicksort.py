def quicksort(list_to_sort):
    result=[]
    if len(list_to_sort)<=1:
        return list_to_sort
   #结束条件
    al=[]
    ar=[] 
    pivotplace=0
    def partition(list_to_sort):
        x=list_to_sort[0]
        #pivot
        i=0
        for j in  range(1,len(list_to_sort)):
            if list_to_sort[j]<=x:
                i=i+1
                temp=list_to_sort[i]
                list_to_sort[i]=list_to_sort[j]
                list_to_sort[j]=temp
                #exch: a[i] a[j]
        temp=list_to_sort[0]
        list_to_sort[0]=list_to_sort[i]
        list_to_sort[i]=temp
        #exch a[p] a[i]
#         pivotplace=i
        #result[i]=a[i]
        return i
    pivotplace= partition(list_to_sort)  
    al=list_to_sort[0:pivotplace]  
    al=quicksort(al)
    
    ar=list_to_sort[pivotplace+1:]  
    ar=quicksort(ar)
    return al+[list_to_sort[pivotplace]]+ar

a=[6, 5, 3, 1, 8, 7, 2, 4]
print(quicksort(a))