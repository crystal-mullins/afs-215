#define a function
# def func1():
#    print ("I am learning Python function")
#    print ("still in func1")
   
# func1()

# def square(x):
#   	return x*x
# print(square(4))

# def multiply(x,y=0):
# 	print("value of x=",x)
# 	print("value of y=",y)
    
# 	return x*y
  
# print(multiply(y=2,x=4))

# assignment 1 write a function to print the perfect number
# Python Program to find Perfect Number using For loop

Number = int(input(" Please Enter any Number: "))
Sum = 0
for i in range(1, Number):
    if(Number % i == 0):
        Sum = Sum + i
if (Sum == Number):
    print(" %d is a Perfect Number" %Number)
else:
    print(" %d is not a Perfect Number" %Number)