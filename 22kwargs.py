
#!     kwargs : parameter that will pack all the arguments to a dictionary
             #* useful so a function can accept a varying amount of arguments
            #* the double asterisk means that is a kwarg
def info(**names):
    print("your name is")
    names.update({'address':'amman'})
    names.pop('family')
    names.update({'last':'mustafa'})
    for k,v in names.items():
        print(v)

info(first='salem',middle='asad',last='mahmmod',family='obyat',number=501)