def solicitar_matriz() -> list:
    """ 
        Función que solicita los valores de la matriz al usuario
        Args:
            None
        Return:
            list: matriz ingresada por el usuario
    """
    
    # Variable que contendrá la matriz ingresada por el usuario
    resultado = []
    
    # Creamos un bucle 4x4 para solicitar los valores de la matriz
    for i in range(4):
        columna = []
        for x in range(4):
            numero = input("Ingrese el valor del elemento a" + str(i+1) + str(x+1) + ": ")
            if numero == "":
                numero = 0
            columna.append(numero)
        resultado.append(columna)
    return resultado

def imprimir_matriz(matriz: list):
    """ 
    Función que recorre la matriz e imprime cada fila
    Args:
        matriz (list): matriz a imprimir
    Return: 
        None
    """
    
    # Recorremos la matriz e imprimimos cada fila
    for row in matriz:
        print(row)

def pivoteo(matriz, i):
    """ 
    Función que realiza el pivoteo parcial de la matriz
    Args:
        matriz (list): matriz a pivotear
        i (int): indice de la columna
    Return:
        list: matriz pivoteada
    """
    pivote = '%.2f' % 0
    temp = ''
    
    # Creamos un bucle for para obtener el pivote de la columna
    for l in matriz[i:4]:
        if abs(float(l[i])) > abs(float(pivote)):
            pivote = l[i]
            temp = l
    
    # Si el pivote es 0, el sistema no tiene solución única
    if pivote == "0.00":
        print("El sistema no tiene solución única")
        exit(0)
    
    matriz.remove(temp)
    matriz.insert(i, temp)
    return matriz

def reducion_gaussiana(matriz, i):
    """ 
    Función que realiza la reducción gaussiana de la matriz
    Args:
        matriz (list): matriz a reducir
        i (int): indice de la columna
    Return:
        list: matriz reducida
    """
    
    # Creamos un bucle for para realizar la reducción gaussiana
    for x in range(i+1, 4):
        
        # El pivote es el elemento de la diagonal principal
        pivote = matriz[i][i]
        constante = float(matriz[x][i]) / float(pivote)
        for y in range(i,4):
            matriz[x][y] = float(matriz[x][y]) - (constante * float(matriz[i][y]))
            
        # Si la fila tiene 4 ceros, el sistema no tiene solución única
        if matriz[x].count(0) == 4:
            print("El sistema no tiene solución única")
            print(matriz[x])
            exit(1)
            
    return matriz


if __name__ == '__main__':
    
    # Solicitamos la matriz al usuario
    matriz_inicial = solicitar_matriz()
    
    # Recorremos la matriz para realizar el pivoteo parcial escalado
    for i in range(3):
        matriz_inicial = pivoteo(matriz_inicial, i)
        matriz_inicial = reducion_gaussiana(matriz_inicial, i)
        
    # Imprimimos la matriz resultante
    imprimir_matriz(matriz_inicial)    