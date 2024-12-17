def bubble_sort(lst):
    for j in range(len(lst)-1):
        for i in range(len(lst)-1):
            if lst[i+1]<lst[i]:
                swap=lst[i+1]
                lst[i+1]=lst[i]
                lst[i]=swap
    return lst
# print(bubble_sort([200,100,300,400,500]))
def bubble_sort_recursion(lst1,n):
    if n==0:
        return lst1
    for i in range(len(lst1)-1):
        if lst1[i+1]<lst1[i]:
            swap=lst1[i]
            lst1[i]=lst1[i+1]
            lst1[i+1]=swap
    return bubble_sort_recursion(lst1,n-1)
#bubble sort takes o(n^2) for both iterative method and recursive method and it takes o(n) space complexity
lst1=[20,11,2,5,8,38,1]
n=len(lst1)-1
print(bubble_sort_recursion(lst1,n))
