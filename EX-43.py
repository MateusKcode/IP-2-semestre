# @cikey eb34e327288c5f9052179536061c4901
# @sid 20251174010031
# @aid V4.3


#begin_inputs
mes = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
#end_inputs
for m in mes:
    if m(1, 13):
        print(mes)
    else: 
        print("mes invalido")
