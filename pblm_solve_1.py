# 1. 'write a code for counting set bits and unset bits for a binary number of a number. setbits=1,unsetbits=0 '
def bitcount(a):
    setbitcount=0
    unsetbitcount=0
    while a>0:
        if a&1==1:
            setbitcount+=1
        else:
            unsetbitcount+=1
        a=a>>1
    print(f'setbits={setbitcount}')
    print(f'unsetbits={unsetbitcount}')
# a=int(input('Enter a number: '))
# bitcount(a)
# ------------------------------------------
# 2.write a recursive code for multiplication table without using * operator
def mult(a,b):
    if b==0:
        return 0
    elif b<0:
        return -(a+mult(a,b+1))
    else:
        return a+mult(a,b-1)
# prod=mult(3,1)
# print(prod)
# ---------------------------------------
# 3. search an element in the list. using the dictionary conversion method.
l=[10,7,9,5,11,2]
mydict={item:True for item in l}
# print(mydict)
def search_item(element,list):
    if element in mydict:
        return mydict[element]
    else:
        return False
# print(search_item(100,l))
# 4. power function implement through recursive approach.
def power(a,n):
    if n==0:
        return 1
    elif n<0:
        return 1/power(a,-n)
    elif n%2==0:
        res=power(a,n//2)
        return res*res
    elif n%2!=0:
        res1=power(a,n//2)
        return res1*res1*a


print(power(2,-2))