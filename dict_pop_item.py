# write a programme to create a popitem() function in dict
def pop_item(d):
    for i,v in d.items():
        last_element=i
    tmp=d[last_element]
    del d[last_element]
    return last_element,tmp
d={1:'m',2:'u',3:'r',4:'l'}
# print(pop_item(d))
# print(d)

def pop_fun(d,key):
    deleted_item=d[key]
    del d[key]
    return key,deleted_item
d={1:'m',2:'u',3:'r',4:'l'}
# print(pop_fun(d,2))
# print(d)

def common_elements(lst1,lst2):
    if len(lst1)<=len(lst2):
        d1={}
        for i in lst1:
            d1[i]=1
        lst3=[]
        for i in lst2:
            if i in d1:
                lst3.append(i)
    else:
        if len(lst2)<=len(lst1):
            d1={}
            for i in lst2:
                d1[i] = 1
            lst3 = []
            for i in lst1:
                if i in d1:
                    lst3.append(i)
    return lst3

lst1=[34,56,78,90,12,34]
lst2=[45,56,90,77,88,12,49,50,61]
print(common_elements(lst1,lst2))

