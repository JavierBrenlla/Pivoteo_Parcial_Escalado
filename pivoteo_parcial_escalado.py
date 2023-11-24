def solicitar_matriz():
    resultado = []
    for i in range(4):
        columna = []
        for x in range(4):
            elemento = "a" + str(i+1) + str(x+1)
            numero = input("Ingrese el valor del elemento a" + str(i+1) + str(x+1) + ": ")
            if numero == "":
                numero = 0
            columna.append(numero)
        resultado.append(columna)
    return resultado

def imprimir_matriz(matriz):
    for row in matriz:
        print(row)

def pivoteo(matriz, i):
    pivote = '%.2f' % 0
    aux = ''
    for l in matriz[i:4]:
        if abs(float(l[i])) > abs(float(pivote)):
            pivote = l[i]
            aux = l
            
    if pivote == "0.00":
        print("El sistema no tiene solución única")
        exit(0)
    
    matriz.remove(aux)
    matriz.insert(i, aux)
    return matriz

def reducion_gaussiana(matriz, i):
    for x in range(i+1, 4):
        pivote = matriz[i][i]
        constante = float(matriz[x][i]) / float(pivote)
        for y in range(i,4):
            matriz[x][y] = float(matriz[x][y]) - (constante * float(matriz[i][y]))
            
        if matriz[x].count(0) == 4:
            print("El sistema no tiene solución única")
            print(matriz[x])
            exit(1)
            
    return matriz


if __name__ == '__main__':
    matriz_inicial = solicitar_matriz()
    
    for i in range(3):
        matriz_inicial = pivoteo(matriz_inicial, i)
        matriz_inicial = reducion_gaussiana(matriz_inicial, i)
        
    imprimir_matriz(matriz_inicial)
        