#for and while loops

#1.loops are used to repeat instruction
count=1
while count<=7:
    print("hello")
    count +=1

print(count)    

i=1
while i<=4:
    print("apni kaksha")
    i +=1

#que1

a=1
while a<=100:
    print(a)
    a +=1    

#que2

b=100
while b>=1:
    print(b)
    b -=1    

#que3
n=int(input("enter any number :"))
c=1
while c<=10:
    print(n*c)    
    c +=1

#que4

nums=[1 ,4 ,9 ,16,25,36,49,64,81,100]

index=0
while index<len(nums):
    print(nums[index])
    index +=1

#break

e=1
while e<=6:
    print(e)
    if(e ==4):
        break
    e +=1

#for loop

veggies=["capsi","bean","soya","beet","carrot"]

for val in veggies:
    print(val)
else:
      print("end")  

#que1
list1=[1,4,9,16,25,36,49,64,81,100]      

for el in list1:
    print(el)

#que2
index=0
x=64
for el in list1:
    if(el == x):
        print("found at index",index)
    index +=1

#range
j=int(input("enter number:"))
seq =range(1,11)

for q in seq:
     print(q*j)

#que1

n=6
sum=0
for r in range(1,n+1):
    sum +=r
    print( sum)



    