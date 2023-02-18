class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        colores = ["rojo", "negro", "blanco", "amarillo", "verde"]
        if color in colores:
            self.color = color
        

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo


class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        return len(self.asientos)
    
    def verificarIntegridad(self):
        if self.regitro != self.motor.registro:
            return "Las piezas no son originales"
        for i in self.asientos:
            if i.registro != self.registro:
                return "Las piezas no son originales"
                break
        return "Auto original"
if __name__=="__main__":
    asiento1 = Asiento("rojo", 23045, 2442545)
    a = str(type(asiento1))
    if "Asiento" in a:
        print(25)