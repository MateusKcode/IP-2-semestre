# @cikey eb34e327288c5f9052179536061c4901
# @sid 20251174010031
# @aid V7.1

from string import ascii_lowercase

#begin_inputs
letras = ['a', 'b', 'c']
#end_inputs

from string import ascii_lowercase

def letras_disponíveis(letras_usadas):
    alfabeto = list(ascii_lowercase)
    
    disponiveis = [letra for letra in alfabeto if letra not in letras_usadas]
    return disponiveis

print(letras_disponíveis(letras))

