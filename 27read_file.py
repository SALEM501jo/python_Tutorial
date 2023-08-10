 
try:
    with open('C:\\Users\\NTC\\Desktop\\test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")


