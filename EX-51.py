# @cikey eb34e327288c5f9052179536061c4901
# @sid 20251174010031
# @aid V5.1


#begin_inputs
 

#end_inputs

somatorio = 0
peso = int(input('Digite o peso:'))
somatorio += peso
while somatorio <= 500:
    peso = int(input('Digite o peso:'))
    somatorio += peso
print('Peso excedido')