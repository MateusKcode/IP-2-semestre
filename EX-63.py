# @cikey eb34e327288c5f9052179536061c4901
# @sid 20251174010031
# @aid V6.3


#begin_inputs
n = int(input())
#end_inputs

def reverso(n):
    return int(str(n)[::-1])

print(reverso(n))