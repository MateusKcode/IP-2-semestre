# @cikey eb34e327288c5f9052179536061c4901
# @sid 20251174010031
# @aid V3.4


#begin_inputs
# programa sem entrada (input)
#end_inputs
for ano in range(2017, 2021):
    for mes in range(1, 13):
        for dia in range(1, 30):
            if ano == 2020 and mes == 12 and dia > 30:
                break
            print(f"{dia}/{mes}/{ano}")
	
