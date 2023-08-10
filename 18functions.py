
#!functions : a block of code that will be executed only if its called

#*this is the header of the function
def hello(name,num1,num2):#* these called parameters they are variables that u will give them a value when the function is called
#* def stands for define 
    #* hello is the name of the function you can call it whatever you want
    print("Hello, " + str(name) + "!")
    print(num1 + num2)#*this is the body of the function

#* this is how to call the function
hello("salem",num1=10,num2=8)#* these are arguments we put them to give the variables value
#*hello is the name of the function 

#!press run to see the results