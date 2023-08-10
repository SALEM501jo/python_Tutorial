
#! exception : events detected during execution that interrupt the flow of the program

number=5

try: #* when the code is risky or could break the flow of the program we srround the code with a (try) block
    num1=int(input("enter the first number"))
    num2=int(input("enter the second number"))
    result= num1/num2
except TypeError:
       #* the name of the exception
    print("you can't add a number to a string")

except ZeroDivisionError:
    print("you cant divide by zero")

except Exception:
       #* for any exception its not recommended to put it in the first except 
    print("Something went wrong")

else: #* if there is no exception then else would execute 
    print(result)

finally: #*whether there is a exception or not it will execute anyway
    print("its done")

    

