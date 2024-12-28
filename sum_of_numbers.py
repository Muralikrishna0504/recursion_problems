# write a programme to find the pairs that gives the sum of the given number
def pairs_sum(lst):
    count=0
    for i in lst:
        for j in lst:
            if i+j==9:
                count+=1
    return count
lst=[4,5,8,1,3,2]
# print(pairs_sum(lst))

# class address:
#
#     def objectadress(self):
#         print(id(self))
# obj1=address()
# obj1.objectadress()
# print(id(obj1))
# print(obj1)
# class employee:
#     eid=None
#     ename=None
# emp=employee()
# emp.eid=1
# emp.ename='Murali'
# print(emp)
# print(emp.eid)
# emp.salary=20000
# print(emp.salary)
# class emp:
#     def __init__(self):
#         self.eid=1
#         self.ename='Murali'
#     def display(self):
#         print(self.eid)
#         print(self.ename)
# obj2=emp()
# obj2.display()
# obj2.ename='nikhil'
# obj2.display()