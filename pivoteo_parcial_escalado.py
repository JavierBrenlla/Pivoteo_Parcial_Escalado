subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

def recoger_matriz():
    rows, cols = (4, 4)
    matriz = []
    for i in range(rows):
        col = []
        for j in range(cols):
            elemento = "a" + str(i+1) + str(j+1)
            num = input("Ingrese el valor del elemento {}: ".format(elemento.translate(subscript)))
            if num == "":
                num = 0
            col.append(num)
        matriz.append(col)
    return matriz

def imprimir_matriz(matriz):
    for row in matriz:
        print(row)

def pivoteo(matriz, i):
    col = str(i+1)
    elemento = ("a" + str(i+1) + str(i+1)).translate(subscript)
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
    for j in range(i+1, 4):
        pivote = matriz[i][i]
        constante = float(matriz[j][i]) / float(pivote)
        for k in range(i,4):
            matriz[j][k] = float(matriz[j][k]) - (constante * float(matriz[i][k]))
            
        if matriz[j].count(0) == 4:
            print("El sistema no tiene solución única")
            print(matriz[j])
            exit(1)
            
    return matriz


if __name__ == '__main__':
    matriz_inicial = recoger_matriz()
    
    for i in range(3):
        matriz_inicial = pivoteo(matriz_inicial, i)
        matriz_inicial = reducion_gaussiana(matriz_inicial, i)
        
    imprimir_matriz(matriz_inicial)
        