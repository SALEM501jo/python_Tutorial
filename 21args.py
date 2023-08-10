
#! args : parameter that will back all the arguments into a tuple
        #*useful so that a function can takes a varying amount of arguments

#def add(*arg):
   # sum=0 #! local variable 
    #for i in arg:#* this for loop will sum the all the arguments
     #   sum+=i
   # return sum 

#print(add(5,6,9,10,11,12,13,14))9

def add(*arg):
    sum=0 
    arg=list(arg) #* if we want to change the arguments we need to do type casting from tuple to list
    arg[3]=8;arg[6]=10
    for i in arg:
        sum+=i
    return sum 

print(add(5,6,9,10,11,12,13,14))

