# Selection sort:
# iterative approach
def selection_sort(lst,n):
    m=0
    for j in range(n-1):
        smallest = lst[m]
        index=m
        for i in range(m+1,n-1):
            if lst[i]<smallest:
                smallest=lst[i]
                index=i
        tmp = lst[m]
        lst[m] = smallest
        lst[index] = tmp
        m=m+1
    return lst
lst=[20,38,32,21,44,2,3,10,19,89]
n=len(lst)
print(selection_sort(lst,n))

# recursive approach
def selection_sort_recursive(lst1,m=0):
    if m==len(lst1):
        return lst1
    smallest=lst1[m]
    index=m
    for i in range(m+1,len(lst1)):
        if lst1[i]<smallest:
            smallest,index=lst1[i],i
    tmp=lst1[m]
    lst1[m]=smallest
    lst1[index]=tmp
    return selection_sort_recursive(lst1,m+1)
lst1=[20,38,32,21,44,2,3,10,19,89]
<<<<<<< HEAD
# print(selection_sort_recursive(lst1))
=======
print(selection_sort_recursive(lst1))
>>>>>>> cb7e20de1413c8349796d10ae044a7f4e458344e
