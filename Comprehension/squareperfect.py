#declarado lista aberta
from typing import Concatenate


squares = []
#percorrendo o valor de 1 a 10
for value in range(1,11):
#cada valor é elevado ao quadrado e armazenado em square
    square = value**2
    # o valor é concatenado e adicionado na lista squares
    squares.append(square)
#quando o laço acaba é postado a lista de quadrados perfeitos
print(squares)

#Para escrever o código mais conciso é só omitir a variavel temporaria 
#squares.append(value**2)
