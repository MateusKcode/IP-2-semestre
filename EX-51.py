# @cikey eb34e327288c5f9052179536061c4901
# @sid 20251174010031
# @aid V5.1


#begin_inputs
soma = 0
while True:
    peso = int(input())
    soma += peso
    if soma > 500:
        print("peso excedido")
        break