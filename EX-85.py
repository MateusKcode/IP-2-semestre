# @cikey eb34e327288c5f9052179536061c4901
# @sid 20251174010031
# @aid V8.4

tel = {}

for n in range(3):
    user = input("Nome:")
    num = input("numero:")
    tel[user] = num    
print(f"{tel}",)
wanted = input("\n""nome que vc quer:")
if wanted in tel:
    print(f"o nome {wanted} está na lista de telefone{tel[user]}")
else:
    print("não tem esse contato na lista")