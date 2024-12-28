def sub_list(lst):
    lst1=[]
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            lst1.append([lst[i:j+1]])
    return lst1
# print(sub_list([1,2,3,4,5]))
def sub_list_recursion(lst,i=0,lst1=[]):
    if i==len(lst):
        return lst1
    for j in range(i,len(lst)):
        lst1.append(lst[i:j+1])
    return sub_list_recursion(lst,i+1,lst1)
# print(sub_list_recursion([1,2,3,4,5]))

def sub_string(s):
    s1=''
    for i in range(len(s)):
        for j in range(i,len(s)):
            s1=s[i:j+1]
            if ispalindrome(s1):
                print(s1)
def ispalindrome(s1):
    i=0
    j=len(s1)-1
    while i<=j:
        if s1[i]!=s1[j]:
            return False
        else:
            i+=1
            j-=1
        return True

s='abccba'
# sub_string(s)
def masking(email):
    s1=''
    s2=''
    for i in range(len(email)):
        if email[i]=='@':
            s1=email[0:i]
            s2=email[i:]
    n=len(s1)
    s1=''
    for j in range(n):
        s1+='#'
    s3=s1+s2
    return s3
# print(masking('python@gmail.com'))

def unique_elem(ss):
    s=''
    i=0
    count=0
    ss=ss+' '
    while i<len(ss)-1:
        j=i+1
        curr=ss[i]
        next=ss[j]
        if curr==next:
            count+=1
        else:
            count+=1
            s += curr
            s += str(count)
            count=0
        i+=1
    return s
print(unique_elem('aaabbbccc'))
def letter_swapping(s):
    s1=s[0]
    s2=s[1]
    s3=s[-1]
    s4=s[-2]
    s[0]=s3
    s[1]=s4
    s[-1]=s1
    s[-2]=s2
    return s
# print(letter_swapping('google'))

def maximum_count(s):
    l=s.split()
    count=0
    word=''
    lst=[]
    for i in l:
        if count<len(i):
            count=len(i)
            word=i
            lst.append((count,word))

    return lst[0],lst[-1]
# print(maximum_count('hi whats going on'))

lst=[(2,'hi'),(5,'whats'),(5,'going'),(2,'on')]
lst.sort()
# print(lst)