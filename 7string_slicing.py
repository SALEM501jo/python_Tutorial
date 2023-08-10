
#! string slicing : create a substring by extracting elements from another string 
#* string slicing methods 1.indexing[] 2.slice() 

#* we have here a list of strings and here is what we need to do
#?1.slice the first string (first_name) to get the ("salem") and (asa'd) in substring 
#?2.extract the name of the website in the string (google),(hidden_wiki)

first_name="salem asa'd"
google="http://google.com"
hidden_wiki="http://hiddenwiki.com"
zero_one="101010101010"

#* we are going to use the two methods
#* first the indexing[]
#![start:stop:step]
#*start is inclusive its the place to start slicing 
#*stop is its the exclusive its the end of the slice
#*step is how much were increasing our index between start and stop

#!first task 
new_name=first_name[:5]
print(new_name)
#output:salem
#* if we want to slice from the start there is no need to write zero length we can leave it empty like this this [:5] 
#* and the same thing if we need to slice to the end we can leave it empty like this [5:]
second_name=first_name[6:]
print(second_name)
#output:asa'd
#!second task
#*if we need to slice something from the end we can start counting the from -1 ...-n like this example
web_name=google[7:-4]
print(web_name)
#output:google
second_web=hidden_wiki[7:-4]
print(second_web)
#output:hiddenwiki
#*we can use step for example if we want to skip the second character like this
one_only=zero_one[::2]
print(one_only)
#output:111111
#*we can use it to reverse the the string
reversed_name=first_name[::-1]
print(reversed_name)
#output:d'asa melas
#*second method is slice()
#*the special in this function is we can reuse it 
#!slice(start,end)

#!first task 
#*we can use them when we need them
new_first=slice(0,5)
second_new=slice(5,11)

print(first_name[new_first])
print(first_name[second_new])
#output:salem
#output:asa'd

#!second task
website_name=slice(7,-4)
facebook="http://facebook.com"
print(facebook[website_name])
print(google[website_name])
print(hidden_wiki[website_name])
#output:google
#output:hiddenwiki
#* if you notice that we use the same slice for two websites strings without the need to write another slice

#* run the program and see the output
#!this is how string slice works in python .

 