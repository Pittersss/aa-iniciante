import sys

input = sys.stdin.readline
print = sys.stdout.write

def preencher_array(rep, array):
    for i in range(rep):
        array.append(0)

def prefix_sum(array_inicial, tamanho_array, array_soma):
    array_soma[0] = array_inicial[0]
    for i in range(1, tamanho_array):
        array_soma[i] = array_soma[i-1] + array_inicial[i]

arr = [-1,3,-2,5,3,-5,2,2]
array_soma = []
preencher_array(8 ,array_soma)
prefix_sum(arr, len(arr), array_soma)
print(str(array_soma) + "\n")

    

