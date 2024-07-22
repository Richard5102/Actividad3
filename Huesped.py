from datetime import datetime

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f"Nombre: {self.nombre} y tiene {self.edad} años"
       
class Huesped(Persona):
    def __init__(self, nombre, edad, habitacion, costoHabitacion, rfc, NumeroDeCuenta, FechaIngreso, HospedadoActualmente, ServicioHabitacion):
        Persona.__init__(self, nombre, edad)
        self.habitacion = habitacion
        self.rfc = rfc
        self.costoHabitacion = costoHabitacion 
        self.NumeroDeCuenta = NumeroDeCuenta 
        self.FechaIngreso = FechaIngreso
        self.HospedadoActualmente = HospedadoActualmente
        self.ServicioHabitacion = ServicioHabitacion


    def costoHabitacion (self):
        costoHabitaciones = {1: 1000.00, 2: 1500.00, 3: 2500}
        return costoHabitaciones.get(self.habitacion, 0)

    def info (self):
        return f"Huesped: {self.nombre}, en habitacion: {self.habitacion}, con RFC: {self.rfc}"
    def __str__ (self):
        return f"Huesped: {self.nombre}, en habitacion: {self.habitacion}, con RFC: {self.rfc}"


    def saldo(self):
        date_format = '%m/%d/%Y'
        ingreso = datetime.strptime(self.FechaIngreso, date_format)
        fechaHoy = datetime.now()
        diasIngresado = (ingreso - fechaHoy).days
        return self.costoHabitacion(self.habitacion) * diasIngresado