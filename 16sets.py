 
#!sets : collection which is unordered ,unindexed and no duplicate values

a={"pizza","mansaf","men"}
S={"coffee","tea","americano","espresso","men"}
#* if we print the set S every time it will print the list with deferent order
#print(S)
#* if we add the same value more than one time it will only  print the value one time because the set doesn't allow duplicate values 
#! remove the # and run the program to see the results
#S={"coffee","tea","americano","espresso","espresso","espresso","espresso"}
#print(S)


#* few useful functions for the set
#* add : it adds value to the set #!note: you can put one value only like this S.add("food") you cant add more than one value in the function
#S.add("water")
#*remove : it removes value from the set
#S.remove("tea")
#* clear : it clears the set
#S.clear()
#* update : it will ad set to another set 
#S.update(a)
#*6.union : it will union two sets together and put them in new set
#newset=S.union(a)
#print(newset)
#*7.difference : it will print the difference between two sets 
#print(a.difference(S))
#*8.intersection : it will print anything they have in common
#print(S.intersection(a))