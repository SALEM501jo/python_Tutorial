
#! key words arguments : arguments preceded by identifier when we pass them to a function
                      #! the order of the arguments does not matter, unlike positional arguments
                      #! python knows the names of the arguments that our function receives

def hello(name1,second,third):
    print("hello "+name1+" "+second+" "+third)

hello(third="the punisher",second="castle",name1="frank")
