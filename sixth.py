#functions and recursion in python

#functions -->block of statement that performs a specific task

def  calc_sum(a,b):
    sum=a+b
    print(sum)
    return sum

calc_sum(4,8)
calc_sum(42,18)
calc_sum(5,21)
calc_sum(4,4)

#1.average of 3 numbers

def calc_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg

calc_avg(2,4,6) 
calc_avg(98,97,95)   

#que1
cities=["pune","mumbai","delhi","calcutta","banaras","noida"]
games=["fifa","soccer","crazygo","mr.beast"]

def print_len(list):
    print(len(list))

print_len(cities)    
print_len(games)

#que3


def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact *=i
        print(fact)

cal_fact(5)        

#que4 -->convert usd to rs

def converter(usd_val):
    inr_value=usd_val * 83
    print(usd_val, "USD=",inr_value, "INR")

converter(2)  
converter(4)  

#hw que1
i=int(input("enter your number :"))

def odd_or_even(i):
    if (i%2==0):
        print("EVEN")
    else:
        print("ODD")    

odd_or_even(i)    

#recursion -->calling a function inside itself is called recursion


   


