def check_sign(a,b):
    if a^b==1:
        return True
    else:
        return False
# print(check_sign(5,6))
def power_of_2(a):
    if a&1==0:
        return True
    else:
        return False
# print(power_of_2(6))
def set_difference(s1,s2):
    d=dict()
    s=set()
    if len(s1)<len(s2):
        for i in s1:
            d[i]=1
        for i in d.keys():
            if i not in s2:
                s.add(i)
    if len(s2)<len(s1):
        for i in s2:
            d[i]=1
        for i in d.keys():
            if i not in s1:
                s.add(i)
    return s
s1={2,3,4,5,6,7}
s2={2,6,7,11,34,56,90}
# print(set_difference(s1,s2))
# ------------------------------------------------------
from selection_sort import selection_sort_recursive
def consecutive_sequence(lst):
    d=dict()
    sorted_list=selection_sort_recursive(lst)
    print(sorted_list)
    i=0
    l = []
    while i<len(sorted_list)-1:
        if sorted_list[i+1]-sorted_list[i]==1:
            if sorted_list[i] not in l:
                l.append(sorted_list[i])
                l.append(sorted_list[i+1])
        else:
            if l:
                d[len(l)]=l
            l=[]
        i+=1
    greater=0
    for i in d.keys():
        if i>greater:
            greater=i
    return d[greater]

lst=[2,3,10,7,8,9,34,36,12,14]
print(consecutive_sequence(lst))