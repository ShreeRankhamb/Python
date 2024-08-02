#Strings & Conditional Statements

str1="This is a string .\n And i would love to learn new sets"
print(str1)
print(len(str1))

#1.slicing

print(str1[1:8])

#2.Replace

print(str1.replace("o","a"))

#practice que1

a=str(input("Enter any name :"))
print(len(a))

#que2
str="i am $ from $ your $ termides"
print(str.count("$"))

#que3

a=int(input("ENter any number :"))

if (a %  2 == 0):
    print("Even")
else:
    print("Odd")    

#que4
l=34
m=20
n=45    

if (l>=m and l>=n):
    print("1st is the greatest no.")
elif(m>=n):
    print("2nd is the greatest no")
else:
    print("3rd is the largest no")      

#que5      

num=int(input("Enter the number: "))

if (num % 7 ==0):
    print("It is multiple of 7")
else:
    print("Not a multiple of 7")    