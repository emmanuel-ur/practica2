

def validar_numero(num):
    if not isinstance(num, (int, float)) or num < 0:
        raise ValueError(" no negativos o r1 .")

def sumar(a, b):
    validar_numero(a)
    validar_numero(b)
    return a + b

def restar(a, b):
    validar_numero(a)
    validar_numero(b)
    return a - b

def multiplicar(a, b):
    validar_numero(a)
    validar_numero(b)
    return a * b

def dividir(a, b):
    validar_numero(a)
    validar_numero(b)
    if b == 0:
        raise ValueError("No se puede dividir por cero we ")
    return a / b

