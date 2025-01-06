def max_word(lst):
    d={}
    for i in lst:
        d[len(i)]=i
    d1=sorted(d)
    return (d[d1[0]],d1[0]),(d[d1[-1]],d1[1])
lst=['world','wor','wrol','word','worlds']
# print(max_word(lst))
import re
# def pattern_search(s):
#     pattern=['\S']
#     result=re.search(pattern,s)
#     print(result)
# # pattern_search('murali krishna Navuluri')
class Student:
    location='Hyderabad'
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
    def display(self):
        print(self.rollno)
        print(self.name)
    @classmethod
    def details(cls):
        return cls.location
    @staticmethod
    def static_class():
        print(Student.location)
s=Student(101,'xyz')
s.display()
print(s.details())
s.static_class()
Student.static_class()

