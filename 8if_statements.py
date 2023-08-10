 
#!if statements: a block of code that will execute if its condition is true and if the condition is false then it will skip the block of code
#* if "the condition" :then the block of code that will execute if its condition is true
#*elif its a shortcut for (else if)
#* else :if all the conditions are false then it will execute else 
#!logical operators :(and,or,not) used to check if two or more conditions are true
#*the operator (and) :the two conditions must be true or it will be false 
#*the operator (or)  : at least one of the conditions must be true or it will be false
#* the operator (not): it will reverse the condition if its true it will be false and the opposite
#!order is very important
temp=int(input("enter the temperature :"))

if temp>=30 and temp<=50:
    fahren=(temp*2)+30
    print("the temperature in fahrenheit is: "+str(fahren))
    print("its a hot day")
elif temp>=20 and temp<=29:
    fahren=(temp*2)+30
    print("the temperature in fahrenheit is: "+str(fahren))
    print("its mostly sunny day")
elif temp>=10 and temp<=19:
    fahren=(temp*2)+30
    print("the temperature in fahrenheit is: "+str(fahren))
    print("its a cold day dont forget your jacket")
elif temp>=5 and temp<=9:
    fahren=(temp*2)+30
    print("the temperature in fahrenheit is: "+str(fahren))
    print("its a very cold day and expected to be raining")
elif temp>=-20 and temp<=4:
    fahren=(temp*2)+30
    print("the temperature in fahrenheit is: "+str(fahren))
    print("its a freezing outside don't go outside")
else:
    print("the temperature you entered is wrong")
 