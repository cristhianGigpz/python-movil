class DragonBallException(Exception):
    """Clase base para las excepciones del módulo Dragon Ball."""
    pass

class ListadoVacioException(DragonBallException):
    """Excepción lanzada cuando una lista esperada no contiene elementos."""
    pass

class ListadoNoEsListaException(DragonBallException):
    """Excepción lanzada cuando un objeto esperado como lista no lo es."""
    pass
