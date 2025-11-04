# @cikey eb34e327288c5f9052179536061c4901
# @sid 20251174010031
# @aid V7.2


#begin_inputs
letras = []
palavra = "abacate"
#end_inputs
chances = 4
ganhou = False

while True:

    for letra in palavra:

        if letra.lower() in letras:
            print(letra, end=" ")
        else:
            print("_", end=" ")

    print(f"Você tem {chances} chances")
    tentativa = input("Escolha uma letra para adivinhar: ")

    letras.append(tentativa.lower())

    if tentativa.lower() not in palavra.lower():

        chances -= 1

    ganhou = True

    for letra in palavra:

        if letra.lower() not in letras:

            ganhou = False

    if chances == 0 or ganhou:

        break

if ganhou:
    print(f"ganhou, a palavra era {palavra}")
else:
    print(f"voce perdeu, a palavra era {palavra}")
