# write a programme to find sum of the first and last element of the digit
def first_and_last(n):
    if n<10:
        return n
    return n%10+first_and_last(n//(10**(len(str(n))-1)))
print(first_and_last(1278954))