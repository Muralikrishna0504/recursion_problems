# write a programme for insertion sort
def insertion_sort(lst):
    i=1
    while i<len(lst):
        print(i)
        j=i-1
        current_element=lst[i]
        while j>=0 and i<len(lst):
            if lst[j]>current_element:
                tmp=lst[j]
                lst[j]=current_element
                lst[i]=tmp
            j-=1
        i+=1

    return lst

lst=[5, 2, 9, 1, 5, 6]
print(insertion_sort(lst))
# def insertion_sort(lst):
#     i = 1
#     while i < len(lst):
#         j = i - 1
#         # Start by storing the current element (lst[i])
#         current_value = lst[i]
#
#         # Move elements of lst[0..i-1] that are greater than current_value
#         # to one position ahead of their current position
#         while j >= 0 and lst[j] > current_value:
#             lst[j + 1] = lst[j]  # Shift element to the right
#             j -= 1
#
#         # Insert the current_value in its correct position
#         lst[j + 1] = current_value
#
#         i += 1
#
#     return lst
#
#
# lst = [5, 2, 9, 1, 5, 6]
# print(insertion_sort(lst))
