# write a programme to find median of two sorted list when combined
def combine_sorted_list(lst1,lst2):
    lst3=[]
    i=0
    j=0
    while i<len(lst1) and j<len(lst2):
        if lst1[i]<lst2[j]:
            lst3.append(lst1[i])
            i+=1
        elif lst2[j]<lst1[i]:
            lst3.append(lst2[j])
            j+=1
    if i>=len(lst1)-1:
        for i in lst2:
            lst3.append(i)
    elif j>=len(lst2)-1:
        for j in lst1:
            lst3.append(j)
    return lst3

def median_of_combine_list(lst1,lst2):
    lst=combine_sorted_list(lst1,lst2)
    low=0
    high=len(lst)-1
    mid=(low+high)//2
    if len(lst)%2==0:
        return (lst[mid]+lst[mid+1])/2
    else:
        return lst[mid]
lst1=[1,3,5,7]
lst2=[2,4,6,8]
print(median_of_combine_list(lst1,lst2))
