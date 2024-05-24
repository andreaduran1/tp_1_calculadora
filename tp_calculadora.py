# Alumna: Andrea Duran
# Comision: 312

# Trabajo practico N1:
#     Hacer una calculadora. Para ello el programa iniciará y contará con un menú de opciones:
#     1. Ingresar 1er operando (A=x)
#     2. Ingresar 2do operando (B=y)
#     3. Calcular todas las operaciones
#     a) Calcular la suma (A+B)
#     b) Calcular la resta (A-B)
#     c) Calcular la división(A/B)
#     d) Calcular la multiplicación(A*B)
#     e) Calcular factorial(A!)
#     4. Informar resultados
#     a) “El resultado de A+B es: r”
#     b) “El resultado de A-B es: r”
#     c) “El resultado de A/B es: r” o “No es posible dividir por cero”
#     d) “El resultado de A*B es: r”
#     e) “El factorial de A es: r1 y El factorial de B es: r2”
#     5. Salir
#     • Todas las funciones matemáticas del menú se deberán realizar en una biblioteca aparte,que contenga las funciones
#     para realizar las cinco operaciones.
#     • En el menú deberán aparecer los valores actuales cargados en los operandos A y B(donde dice “x” e “y” en el ejemplo,
#     se debe mostrar el número cargado)
#     • Deberán contemplarse los casos de error (división por cero, etc.)
#     • Documentar todas las funciones

from os import system
from funciones import *



def menu(a,b)->str:
    print("\nCalculadora:")
    print(f"1. Ingresar 1er operando (A={a})")
    print(f"2. Ingresar 2do operando (B={b})")
    print("3. Calcular todas las operaciones\n a)Calcular la suma (A+B)\n b)Calcular la resta (A-B)\n c)Calcular la division (A/B)\n d)Calcular la multiplicación (A*B)\n e)Calcular el factorial(A!)")
    print("4. Informar resultados")
    print("5. Salir\n")

def calculadora():
    
    a = "x"
    b = "y"
    flag_primer_operando = False
    flag_segundo_operando = False
    flag_calculado = False
    resultados = {}

    while True:

        menu(a,b)
        opcion = input("Ingrese una opción: ")

        match opcion:
            case "1":
                while True:
                    try:
                        a = int(input("Ingrese el primer operando: "))
                        break
                    except ValueError:
                        print("Por favor, ingrese un número entero.\n")
                flag_primer_operando = True

            case "2":
                if flag_primer_operando == True:
                    while True:
                        try:
                            b = int(input("Ingrese el segundo operando: "))
                            break
                        except ValueError:
                            print("Por favor, ingrese un número entero.\n")
                    flag_segundo_operando = True
                else:
                    print("Primero deberás ingresar el primer operando\n")
                
            case "3":
                if flag_segundo_operando == True:
                    resultados['suma'] = sumar(a, b)
                    resultados['resta'] = restar(a, b)
                    resultados['division'] = dividir(a, b)
                    resultados['multiplicacion'] = multiplicar(a, b)
                    resultados['factorial_a'] = factorial(a)
                    resultados['factorial_b'] = factorial(b)
                    print("Operaciones calculadas.\n")
                    flag_calculado = True
                else:
                    print("Para calcular deberás ingresar todos los operandos\n")
            
            case "4":
                if flag_calculado == True:
                    print(f"a) El resultado de A+B es: {resultados.get('suma', 'No calculado')}")
                    print(f"b) El resultado de A-B es: {resultados.get('resta', 'No calculado')}")
                    resultado = resultados.get('division', 'No calculado')
                    if isinstance(resultado, str):
                        print(f"c) {resultado}")
                    else:
                        print(f"c) El resultado de A/B es: {resultado}")
                    print(f"d) El resultado de A*B es: {resultados.get('multiplicacion', 'No calculado')}")
                    print(f"e) El factorial de A es: {resultados.get('factorial_a', 'No calculado')} y El factorial de B es: {resultados.get('factorial_b', 'No calculado')}\n")
                    flag_calculado = False
                else:
                    print("Primero deberás calcular las operaciones para obtener los resultados.\n")

            case "5":
                print("Saliendo de la calculadora.")
                break

            case _:
                print("La opción no es válida. Intenta de nuevo.")
                
        

    print("Fin del programa")

calculadora()