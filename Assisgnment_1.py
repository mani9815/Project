## Module 1
## Assignment 1.1

## 1. Create 2 tuples 

tuple1=(10,20,30)
tuple1

tuple2=(40,50,60)
tuple2

## a. concatinate both tuple and store it in t_combine

t_combine = tuple1 + tuple2
t_combine

## b. Repeat the element of t_combine 3 times

t_combine * 3


## c. Access the 3rd element of t_combine

t_combine[2]


## d. Access the first 3 element from t_combine

t_combine[:3]


## e. Access the last 3 element from t_combine

t_combine[-1:-4:-1]


## 2. Create my_list with

## a. First element is tuple with (1,2,3)

my_list =[(1,2,3)]
my_list

## b. Second element is tuple with value (a,b,c)

my_list.append(("a","b","c"))
my_list

## c. Third element is tuple with value (True,false)

my_list.append((True,False))
my_list


## 3. Append new tuple (1,"a",True) in my_list

my_list.append((1,"a",True))
my_list


## 4. Create dictionary name fruit with 

## a,B

fruit = {'Apple':85 ,'Banana':54 ,'Mango':120 ,'Guava':70}
fruit


## c Extract all keys

fruit.keys()


## d. Extract all values

fruit.values()



## 5. create a set named my_set with values (1,1,a,a,True,True)

my_set ={1,1,"a","a","True","True"}
print (my_set)



## Assignment 1.2

## 1. Create two lists L1 & L2, where L1 has values (1,2,3,4,5,6) & L2 has (6,5,4,3,2,1)

L1 =[1,2,3,4,5,6]
L1

L2=[6,5,4,3,2,1]
L2


# a. Compare the corresponding element values of both the lists and print "L1 value is greater than
# L2 element value

for i in range(len(L1)):
    if L1[i] > L2[i]:
        print ("Value of L1 element is greater than L2")
    else:
        print ("Value of L2 element is greater than L1")
        
# 2. Create tuple (10,20,30,40,50,60)
        
tuple3 = (10,20,30,40,50,60)
tuple3        

tuple(i+5 for i in tuple3)


# 3. Create UDF "add_10()" to add 10 

def add_10(number):
    return number + 10

add_10(20)
add_10(5)


# 4. Create UDF "Check_odd_even"

def Check_odd_even(number):
    if number % 2==0:
        print ("The number is even")
    else:
        print ("The number is odd")
        
Check_odd_even(5)
Check_odd_even(4)
