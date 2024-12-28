def binary_toggle(n):
    print(bin(n))
    n1=n^255
    print(bin(n1))
    return n1
# print(binary_toggle(5))
def set_bit_toggle(n,count=0):
    if n==0:
        return n,count
    n=n>>1
    return set_bit_toggle(n,count+1)
# print(set_bit_toggle(5))

def pattern_search(text,pattern):
    n=len(text)
    m=len(pattern)
    for i in range(n-m+1):
        if text[i:i+m]==pattern:
            return i,i+m-1
    return None
print(pattern_search('Hello world!','Hello'))


