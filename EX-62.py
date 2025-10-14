# @cikey eb34e327288c5f9052179536061c4901
# @sid 20251174010031
# @aid V6.2


#begin_inputs
n = int(input())
#end_inputs

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()
