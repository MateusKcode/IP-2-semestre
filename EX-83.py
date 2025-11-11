# @cikey eb34e327288c5f9052179536061c4901
# @sid 20251174010031
# @aid V8.3

with open("Bloco 82.txt","r",encoding="utf-8") as arquivo_original:
    conteudo = arquivo_original.read()
with open("Bloco 83.txt","w",encoding="utf-8") as copiar:
     copiar.write(conteudo)  
print("Arquivo copiado com sucesso")