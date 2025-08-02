def solicita_numeros():
    n = []
    for i in range(10):
        n.append(int(input(f"Digite o numero {i+1} numeros: "))) 
    
    return n

def eh_par(num):
    return num % 2 ==0
    return True

def media_pares(soma, quant):
   print(f"A media e: {soma/quant}")

def ordena_vetor(vetor):
    
    vetor_ordenado = sorted(vetor)
    print(f"O vetor ordenado e: {vetor_ordenado}")

solicitar = solicita_numeros()

contador = 0
soma = 0
for numero in solicitar:
    if eh_par(numero):
        soma += numero
        contador += 1

media_pares(soma, contador)
ordena_vetor(solicitar)
