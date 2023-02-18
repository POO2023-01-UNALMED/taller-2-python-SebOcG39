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
        contador = 0
        for i in self.asientos:
            tipo = str(type(i))
            if "Asiento" in tipo:
                contador += 1
        return contador
    
    def verificarIntegridad(self):
        tipo = str(type(self.motor))
        if "Motor" in tipo:
            if self.regitro != self.motor.registro:
                return "Las piezas no son originales"
        else:
            return "Las piezas no son originales"
        for i in self.asientos:
            tipoA = str(type(i))
            if "Asiento" not in tipoA:
                continue
            if i.registro != self.registro:
                return "Las piezas no son originales"
                break
        return "Auto original"