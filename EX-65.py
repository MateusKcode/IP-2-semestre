# @cikey eb34e327288c5f9052179536061c4901
# @sid 20251174010031
# @aid V6.5

import random

def megasena():
    nummegasena = random.randint(1, 100)
    while True:
        palpite = int(input("Digite um numero entre 1 e 100: "))

        if palpite < nummegasena:
            print("O numero secreto e MAIOR.")
        elif palpite > nummegasena:
            print("O numero secreto e MENOR.")
        else:
            print(f"Parabens! Você acertou! O numero secreto era {nummegasena}.")
            break

megasena()