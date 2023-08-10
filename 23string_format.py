
#*string format : optional methods that gives the users more control when displaying the output
#! remove the # from the code and run the program to see the results
color="red"
sky="blue"
rain="rain"
number=1000
bi=3.14159

                    #* the first {} will be the the first argument and the second will be the second argument                  
print("The color is {} and the sky is {}".format(color,sky))
                       
#print("i love the color {1}, and i hate {0}".format(color,sky))#* positional arguments

#print("i love the color {var2}, and i hate {var1}".format(var1="red",var2="blue"))#* dictionary
                       
#print("i love the {:>10} but i hate getting wet ".format(rain) )
                    #* how many spaces between rain and the next word
                     #* ( 10 ) this is the width of the rain
                    #* ( > ) this to make space after the rain  
                    #* (  < ) this to make space before the rain
                    #* ( ^ ) this to make space in the middle of the rain 
                    #! change the symbol and run the program to see the result
#?print("the number is {:.2f}".format(bi))
                       #* if we want to print the first two numbers after the decimal ( . ) is for the decimal 
                       #*( 2 ) how many numbers to print
                       #* ( f ) this stands for float 
#?print("the number is {:,}".format(number))
                       #* this will add a comma to the number
#print("the number is {:b}".format(number))
                       #* this will print the number in binary
#print("the number is {:o}".format(number))
                       #* this will print the number in octal
#print("the number is {:x}".format(number))
                       #* this will print the number in hexadecimal
#print("the number is {:e}".format(number))
                       #* this will print the number in scientific notation



#? question whats the output of this code
#text=" i will be the best {var:^8} in the world"
#print(text.format(var="programer"))
                   