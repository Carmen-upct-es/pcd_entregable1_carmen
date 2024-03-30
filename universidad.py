"""
Implementacion de un sistema de gestión universitario.
"""

from enum import Enum

class Persona:
    def __init__(self, nombre, dni, direccion, sexo):
        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion
        self.sexo = sexo
    
    def __str__(self):
        return f"Nombre: {self.nombre} \nDNI: {self.dni} \nDirección: {self.direccion} \nSexo: {self.sexo}"

class Departamento(Enum):
    DIIC = 1
    DITEC = 2
    DIS = 3

class Profesor(Persona):
    def __init__(self, nombre, dni, direccion, sexo, creditos, años_servicio, limite_creditos, departamento):
        super().__init__(nombre, dni, direccion, sexo) # profesor toma los atributos de Persona
        self.creditos = creditos
        self.años_servicio = años_servicio
        self.limite_creditos = limite_creditos
        self.asignaturas = list()
        self.departamento = departamento

    def cambiar_departamento(self, otro_departamento):
        self.departamento = otro_departamento
    
    def ganar_creditos(self, nuevos_creditos):
        self.creditos += nuevos_creditos

class ProfesorTitular(Profesor):
    def __init__(self, nombre, dni, direccion, sexo, creditos, años_servicio, limite_creditos, departamento):
        super().__init__(nombre, dni, direccion, sexo, creditos, años_servicio, limite_creditos, departamento)
        self.rol = "Profesor Investigador"
    
    def __str__(self):
        return super().__str__() + f"\nAsignaturas impartiendo: {' '.join(self.asignaturas)}"

class ProfesorAsociado(Profesor):
    def __init__(self, nombre, dni, direccion, sexo, creditos, años_servicio, limite_creditos, departamento):
        super().__init__(nombre, dni, direccion, sexo, creditos, años_servicio, limite_creditos, departamento)
    
    def __str__(self):
        return super().__str__() + f"\nAsignaturas impartiendo: {' '.join(self.asignaturas)}"
    
    
class Estudiante(Persona):
    def __init__(self, nombre, dni, direccion, sexo, grado, curso_actual, años_cursados, creditos):
        super().__init__(nombre, dni, direccion, sexo) # el alumno toma los atributos de Persona
        self.grado = grado
        self.curso_actual = curso_actual
        self.años_cursados = años_cursados
        self.creditos = creditos
        self.asignaturas = list()

    def matricularse_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def aprueba_asignatura(self, asignatura):
        if asignatura in self.asignaturas:
            self.creditos += asignatura.creditos
            self.asignaturas.remove(asignatura)

    def quitar_asignatura_aprobada(self, asignatura):
        if asignatura in self.asignaturas:
            self.asignaturas.remove(asignatura)
    
    def ganar_creditos(self, nuevos_creditos):
        self.creditos += nuevos_creditos
    
    def __str__(self):
        return super().__str__() + f"\nAsignaturas matriculad@: {' '.join(self.asignaturas)}"

          
class Asignatura:
    def __init__(self, nombre, creditos, campo, dificultad):
        self.nombre = nombre
        self.creditos = creditos
        self.campo = campo
        self.dificultad = dificultad


# Probamos el código:
if __name__ == "__main__":

    #asignatura = Asignatura("Fisica", 6, "Ciencias Puras", "7-8")
    investigador = ProfesorTitular("Enriqueta", "256234189L", "Perico Molino", "F", 96, 2, 200, 1)
    print(investigador)
    print()
    estudiante = Estudiante("Mario", "256234189O", "Gato Mojado", "M", "Ingenieria Aeroespacial", 3, 2, 72)
    estudiante.ganar_creditos(6)
    print(estudiante)