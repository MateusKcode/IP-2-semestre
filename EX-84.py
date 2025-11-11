# @cikey eb34e327288c5f9052179536061c4901
# @sid 20251174010031
# @aid V8.4

Dados = {}
with open("Bloco 84.txt","w",encoding="utf-8") as dados:
   for n in range(5):
     Nome = input("Escreva seu Nome:")
     Cpf =  input("Escreva seu CPF:")
     Dados[Nome] = Cpf
     dados.write(f"{Nome};{Cpf}\n")
print("_______________________")
with open("Bloco 84.txt","r",encoding="utf-8") as leia:
    ler = leia.read()
    print(ler.strip())