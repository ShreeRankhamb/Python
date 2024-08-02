#Dictionary and set in python

#1.Dictionaries are the data values that store data in the form of "key:value" pairs

info ={
    "name":"shree",
    "age":20,
    "cgpa":9.4,
    "college":"TCOER",
}
print(info)

#2.nested dictionaries

student = {
    "mame":"ravi",
    "subjects":{
        "phy":77,
        "chem":95,
        "bio":89
    }   
}
print(student["subjects"])
print(student)
print(student.keys())

#set --> is the collection of unordered items(each item must be unique)

collection={"sf","df","fg","hj",65,55,3}
print(collection)
print(type(collection))
print(len(collection))

#set methods

set={1,2,3}
set.add(4)
set.add(5)   # by set.remove(5) we can remove the element
set.add(6)

print(set)
print(len(set))

#a. UNION
set1={1,2,3,4}
set2={2,3,5,6}
print(set1.union(set2))

#b.intersection
print(set1.intersection(set2))

#que1

dict={
    "cat":"a small animal"
}

#que2

marks={}

x=int(input("enter phy :"))
marks.update({"phy":x})

x=int(input("enter chem :"))
marks.update({"chem":x})

x=int(input("enter math :"))
marks.update({"math":x})

print(marks)
