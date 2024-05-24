
def sumar(a:int, b:int)->int:
    """suma dos numeros enteros

    Args:
        a (int): primer operando de la suma
        b (int): segundo operando de la suma

    Returns:
        int: resultado de la suma
    """    
    return a + b

def restar(a:int, b:int)->int:
    """resta dos numeros enteros

    Args:
        a (int): primer operando de la resta
        b (int): segundo operando de la resta

    Returns:
        int: resultado de la resta
    """    
    return a - b

def dividir(a:int, b:int)->int:
    """divide dos numeros enteros.

    Args:
        a (int): numero dividendo
        b (int): numero divisor

    Returns:
        int: resultado de la division.
    """    
    # Manejo de error de manera preventiva
    if b == 0:
        return "No es posible dividir por cero"
    else:
        return a / b
    
def multiplicar(a:int, b:int)->int:
    """multiplica dos numeros enteros.

    Args:
        a (int): primer operando de la multiplicacion
        b (int): segundo operando de la multiplicacion

    Returns:
        int: resultado de la multiplicacion.
    """ 
    return a * b

def factorial(a:int)->int:
    """calcula el factorial de un numero entero positivo

    Args:
        a (int): numero para calcular su factorial 

    Returns:
        int: resultado del calculo del factorial
    """
    # Manejo de error de manera preventiva
    if a < 0:
        return "No existe el factorial de un negativo"

    else:
        fact = 1
        for i in range(2, a+1):
            fact *= i

        return fact
    