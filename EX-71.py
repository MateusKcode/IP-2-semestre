# @cikey eb34e327288c5f9052179536061c4901
# @sid 20251174010031
# @aid V7.1

from string import ascii_lowercase
 6. #begin_inputs
 7. letras = ['a', 'b', 'c']
 8. #end_inputs
 9. def letras_disponíveis(letras_usadas):
10.     alfabeto = list(ascii_lowercase)
11.     
12.     disponiveis = [letra for letra in alfabeto if letra not in letras_usadas]
13.     return disponiveis
14. 
15. print(letras_disponíveis(letras))

