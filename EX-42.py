# @cikey eb34e327288c5f9052179536061c4901
# @sid 20251174010031
# @aid V4.2


#begin_inputs
contador = 0
 #mantenha esse trecho. o input será manipulado aqui.
#end_inputs
for n in range(10):
    id = int(input())
    if id >= 18:
        contador += 1
print(contador)