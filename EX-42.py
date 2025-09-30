# @cikey eb34e327288c5f9052179536061c4901
# @sid 20251174010031
# @aid V4.2


#begin_inputs
idades = [34, 90, 4, 56, 12, 78, 54, 13, 24, 9]
gen_idades = (i for i in idades)
input = gen_idades.__next__
 #mantenha esse trecho. o input será manipulado aqui.
#end_inputs
for idades in range(10):
    if idades >= 18:
        print(gen_idades)