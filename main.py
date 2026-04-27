import menu
import operacion_matrices
import entrada


def principal():
    while True:
        opcion = menu.mostrar_menu()

        if opcion == 5:
            print("Saliendo del programa. ¡Hasta luego!")
            break

        print("\nPor favor, ingrese la Matriz A:")
        matriz_A = entrada.ingresar_matriz()

        filas_A = len(matriz_A)
        columnas_A = len(matriz_A[0])

        print("\nPor favor, ingrese la Matriz B:")

        if opcion == 1 or opcion == 3:
            matriz_B = entrada.ingresar_matriz(filas_requeridas=filas_A, columnas_requeridas=columnas_A)

        elif opcion == 2:
            matriz_B = entrada.ingresar_matriz(filas_requeridas=columnas_A)

        elif opcion == 4:
            matriz_B = entrada.ingresar_matriz()

        if opcion == 1:
            print("\nResultado de la Suma:")
            resultado = operacion_matrices.suma_matrices(matriz_A, matriz_B)

        elif opcion == 2:
            print("\nResultado de la Multiplicación:")
            resultado = operacion_matrices.multiplicacion_matrices(matriz_A, matriz_B)

        elif opcion == 3:
            print("\nResultado del Producto de Hadamard:")
            resultado = operacion_matrices.producto_hadamard(matriz_A, matriz_B)

        elif opcion == 4:
            print("\nResultado del Producto de Kronecker:")
            resultado = operacion_matrices.producto_kronecker(matriz_A, matriz_B)

        if isinstance(resultado, str):
            print(resultado)
        else:
            entrada.mostrar_matriz(resultado)

if __name__ == "__main__":
    principal()