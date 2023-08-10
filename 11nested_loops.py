
#! nested loops : the inner loops all of its iterations before finishing one loop of the outer loop

rows=int(input("how many rows "))
columns=int(input("how many columns"))
symbol=input("waht is the symbol")

for i in range(rows):
    for j in range(columns):
        print(symbol,end=" ")
    print()