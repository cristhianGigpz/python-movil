import time
def medir_tiempo(func):  # decorador
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo: {fin - inicio:.4f}s")
        return resultado
    return wrapper
