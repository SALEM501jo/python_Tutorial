
#!loop control statements = change a loop execution from its original sequence

#*break : used to terminate the loop entirely
#*continue : skips the next loop execution
#*pass : does nothing , acts like a placeholder

#?break
#! reamove the # and run the program to see the result
#while True:
   # name= input("whats your name")
    #if name!="":
     #   break
    #* if uoy leave the name empty it will repeat the loop execution but if you type something it will break the 
    #* loop and continue the program


#?continue
phone_number="078-240-2911"
#*we have an number with dash characters we want to display the number without the dash using continue statement
#for i in phone_number:
 #   if i=="-":
  #      continue
   # print(i,end="")
#* the if statement will go through the phone number and check if there is a dash to skip it and display the number

#?pass 
#for i in range(1,10):
 #   if i==5:
  #      pass
   # else:
    #    print(i)