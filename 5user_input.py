#user input

name=input("enter your name:")
age=input("enter your age:")
gpa=input("enter your gpa:")

print("your name is:"+name)
print("your age is:"+age)
print("your gpa is:"+gpa)
#! if  we didn't declare the data type (float, int, string) it will be pi default as a string

#! if we want to add a number to the string it will give us an error
 #*print(age+1)


#! this is how to declare the data type
id=str(input("enter your name:"))
old=int(input("enter your age:"))
g=float(input("enter your gpa:"))

#after we declare the data type we can do math operations
print(old+5)
print(g+.4)
print("your name is:"+id)
#! we will do a type cast to the float and integer if we need to add it to the string   
print("your age is:"+str(old))
print("your gpa is:"+str(g))