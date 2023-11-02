class Hora:
    def __init__(self, hora = 0, minuto = 0) -> None:
        self.h = hora
        self.min = minuto

    def __str__(self) -> str:
        return str(self.h) + ":" + str(self.min)
    
    