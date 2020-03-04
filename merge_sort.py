#merge sort
def merge_sort(list_to_sort):
    if len(list_to_sort)==1:
        return list_to_sort
   #结束条件
    al=[]
    ar=[]
    
    al=list_to_sort[0:int(len(list_to_sort)/2)]   
    al=merge_sort(al)
    
    for j in range(int(len(list_to_sort)/2),len(list_to_sort)):
        ar.append(list_to_sort[j])
    ar=merge_sort(ar)

    def merge(al,ar):
        # 两个数组合并
        c=[]
        i=0
        j=0
        while i<len(al) and j<len(ar):
            if al[i]<ar[j]:
                c.append(al[i])
                i=i+1
            else: 
                c.append(ar[j])
                j=j+1
        if i==len(al):       
            for j in range(j,len(ar)):
                c.append(ar[j])
        if j==len(ar):
            for i in range(i,len(al)):
                c.append(al[i])

        return c
    return merge(al,ar)

a=[6, 5, 3, 1, 8, 7, 2, 4,9]
print(merge_sort(a))