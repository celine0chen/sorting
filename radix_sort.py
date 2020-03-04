def get_key(num,ath):
    #ath 从数字最右数为第0位
    return num //(10**ath)% 10
def radix_sort(l):
    result=l
    maxlen=len(str(max(l)))
    for i in range(maxlen):
        s=[[] for i in range(10)]
        for num in result:
            s[get_key(num,i)].append(num)
        result=[]
        for a in s:
            for b in a:
                result.append(b)
    return result
a=[0,2,999,79,31,31,102,871,320,26,999]    
print(radix_sort(a))