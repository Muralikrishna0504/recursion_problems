def swap_count(lst):
    count=0
    for j in range(len(lst)):
        for i in range(len(lst)-1-j):
            if lst[i+1]<lst[i]:
                swap=lst[i+1]
                lst[i+1]=lst[i]
                lst[i]=swap
                count+=1
    return count,lst
print(swap_count([2,-4,45,16,7,3,-6,-8,11]))

def reverse_number(n,k):
    s=''
    s1=str(n)
    s+=s1[k:]
    s+=s1[:k]
    return s
print(reverse_number(123456,3))
