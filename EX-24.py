# @cikey eb34e327288c5f9052179536061c4901
# @sid 20251174010031
# @aid V2.4


#begin_inputs
valor_compra = 100
#end_inputs

avista = valor_compra * 0.91
parcelado5 = valor_compra / 5
parcelado10 = (valor_compra * 1.17) / 10

print(round(avista, 2))
print(round(parcelado5, 2))
print(round(parcelado10, 2))
