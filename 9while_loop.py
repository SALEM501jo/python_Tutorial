
#* while loop: a statement that will execute its block of code as long as its condition remains true 
#* once the condition is false it will escape the loop
#?example 1:
#name=input("enter your name: ")

#while len(name)==0:
 #   print("you can't leave your name empty")
  #  name=input("enter your name: ") 

#print("your name is " + name)    
     
#? example 2:
num1=float(input("enter the first number:"))
oper=input("enter the operation :")
num2=float(input("enter the second number:"))
while oper!="+" and oper!="*" and oper!="/" and oper!="-":
    print("Enter a correct mathematic operation :" )
    oper=input("enter the operation :")

if oper=="+":
    print( "the result is: "+ str(num1+num2))
elif oper=="*":
    print( "the result is: "+ str(num1*num2))    
elif oper=="-":
    print( "the result is: "+ str(num1-num2))     
elif oper=="/":
    while num2==0:
          print("you cant divide by zero" )
          num2=float(input("enter the second number:"))
          
    print( "the result is: "+ str(num1/num2))