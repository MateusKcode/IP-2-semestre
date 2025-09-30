# @cikey eb34e327288c5f9052179536061c4901
# @sid 20251174010031
# @aid V5.1


#begin_inputs
pesos = [45, 88, 67, 102, 80, 95, 66]
gen_pesos = (p for p in pesos)
#end_inputs
if pesos >= 500:
    print("peso excedido")
print(gen_pesos)

