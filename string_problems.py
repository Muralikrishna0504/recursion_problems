def beauty(s):
    d=dict()
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
# print(beauty('aabacc'))
from sub_lists import sub_list
def common_sub_string(s1,s2):
    lst1=[]
    lst2=[]
    for i in range(len(s1)-1):
        for j in range(i,len(s1)):
            lst1.append(s1[i:j+1])
    for i in range(len(s2)-1):
        for j in range(i,len(s2)):
            lst2.append(s2[i:j+1])
    # print(lst1,lst2)
    lst3=[]
    for i in lst1:
        if i in lst2:
            lst3.append(i)
    return set(lst3)
print(common_sub_string('abaabccabc','abbbacbabc'))
def pattern_match(s,p):
    n=len(s)
    m=len(p)
    for i in range(n-m+1):
        j=0
        while j<m:
            if s[i+j]!=p[j]:
                break
            j+=1
        if  j==m:
            print(i,j)
# pattern_match('aaabcccaababcaab','caab')

