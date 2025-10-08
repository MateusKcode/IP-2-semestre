# @cikey eb34e327288c5f9052179536061c4901
# @sid 20251174010031
# @aid V5.2


#begin_inputs
 

#end_inputs
minutos = 0
tartaruga = 1 * minutos + 500 
lebre = 10 * minutos

while tartaruga > lebre:
    tartaruga = round(tartaruga + 1)
    lebre = round(lebre + 10)
    minutos += 1
print("{}".format(minutos))
	
