class Data:
    def __init__(self, dia = 1, mes = 1, ano = 2000):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def __str__(self):
        return str(self.dia) + "/" + str(self.mes) + "/" + str(self.ano)


    def add_data(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def valido(self) -> bool:
        if self.dia < 1 or self.dia > 31:
            return False
        
        if self.mes < 1 or self.mes > 12:
            return False
        
        if self.mes == 2:
            if self.bissexto():
                return (self.dia <= 29)
            else:
                return (self.dia <= 28)
        
        if (self.mes == 4) or (self.mes == 6) or (self.mes == 9) or (self.mes == 11):
            return (self.dia <= 30)
        
        return True
    
    def bissexto(self) -> bool:
        ano = self.ano

        if ano % 400 == 0:
            return True
        
        if ano % 100 == 0:
            return False
        
        return (ano % 4 == 0)