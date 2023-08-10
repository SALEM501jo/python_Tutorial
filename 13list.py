
#!list : used to store multiple items in a single variable

games=["assissan creed","tomb rider","far cry","gta","call of duty"]

#*we can edit the list and change the items
#games[4]="cod"
#*we changed the item[4] form "call of duty" to "cod" 
#! remove the # and run the program to see the results
#print(games[4])

#*we can print the whole list like this
#print(games)
#* or this

#for i in games:
    #print(i)

#* few useful functions for lists

#1.append: it adds a new item to the list
games.append("battle feild")
#print(games[5])
#2. remove: it removes the item from the list
games.remove("far cry")
#print(games)
#3. pop: it remove the last item from the list
games.pop()
#print(games)
#4. insert : insert a value at a given index
games.insert(0, "hitman 3")
#print(games)
#5. sort: sort the list
games.sort()
#print(games)
#6. clear: remove all items from the list
games.clear()
#print(games)