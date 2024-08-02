#List and tuples

marks=[33 , 67 , 87 ,56 ,89]
print(marks)
print(type(marks))
print(len(marks))

#1.slicing
print(marks[1:4])

#2.list methods

list=["sai","shruti","sneha","sumit"]
list.append("shree")
print(list)

list1=[3,6,2,4,1,5] #alphabets can also be sorted
list1.sort()      #and list1.reverse() for descending order
print(list1)

#3.tuples

tup=(1,2,3,4)
print(tup)
print(type(tup))

#que1

list2=["animal" ,"kabir" ,"freedy"]
print(list2)

#que2
#palindrome is a term where the str or int looks same as of reverse ex:(1,2,1)

#que3
grade=("B","C","A","D","A","A")
print(grade.count("A"))

#que4
grade1=["B","C","A","D","A","A"]
grade1.sort()
print(grade1)
