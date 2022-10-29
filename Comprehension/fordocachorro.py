from typing import ValuesView


##squares = [value**2 for value in range(1,11)]
#print(squares)

pares = [value%2==0 for value in range(1,11)]
print(pares)

pares = [value for value in range(2,11,2)]
print(pares)