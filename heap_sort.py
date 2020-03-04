def exch(l,x,y):
    temp=l[x]
    l[x]=l[y]
    l[y]=temp
def left(i):
    return i * 2 + 1
def right(i):
    return i * 2 + 2
def find_max(arr, length, i):
    l = left(i)
    r = right(i)
    if l >= length: #   无左
        return i
    elif r >= length: # 有左无右
        return i if arr[i] > arr[l] else l
    else: # 有左有右
        m = l if arr[l] > arr[r] else r
        return i if arr[i] > arr[m] else m
def shiftdown(l,length,largest):
    while left(largest) <length:
        newlar=find_max(l,length,largest)
        if newlar!=largest:
            exch(l,newlar,largest)
            largest=newlar 
        else:
            break
    return l
def heapify(l): 
    for i in range(int(len(l)/2)-1,-1,-1):
        newlar=find_max(l,len(l), i)
        if newlar!=i:
            exch(l,i,newlar)
            #pdb.set_trace()
            shiftdown(l,len(l),newlar)
    return l 
def heap_sort(l):
    result=[]
    heapify(l)
    
    for i in range(0,len(l)-1):
        last = len(l)-i-1
        exch(l,0,last)
        shiftdown(l,last,0)
    return l
a=[3.2,1.3,1,0.11,0.13,2,4,0.9,0.7,0.6,0.4,0.12,0.1,2.2,3]
print(heap_sort(a))