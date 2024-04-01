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
    
    def obtener_departamento(self):
        return self.departamento
    
    def ganar_creditos(self, nuevos_creditos):
        self.creditos += nuevos_creditos
    
    def nueva_asignatura(self, nueva_asignatura):
        self.asignaturas.append(nueva_asignatura)

    def eliminar_asignatura(self, asignatura):
        self.asignaturas.remove(asignatura)


class ProfesorTitular(Profesor):
    def __init__(self, nombre, dni, direccion, sexo, creditos, años_servicio, limite_creditos, departamento, area_investigacion):
        super().__init__(nombre, dni, direccion, sexo, creditos, años_servicio, limite_creditos, departamento)
        self.tipo = "Profesor investigador"
        self.area_investigacion = area_investigacion
    
    def __str__(self):
        return super().__str__() + f"\nDepartamento: {self.departamento}" + f"\nAsignaturas impartiendo: {[asignatura.nombre for asignatura in self.asignaturas]}"


class ProfesorAsociado(Profesor):
    def __init__(self, nombre, dni, direccion, sexo, creditos, años_servicio, limite_creditos, departamento, _trabajo_externo):
        super().__init__(nombre, dni, direccion, sexo, creditos, años_servicio, limite_creditos, departamento)
        self.trabajo_externo = _trabajo_externo

    def __str__(self):
        return super().__str__() + f"\nDepartamento: {self.departamento}" + f"\nAsignaturas impartiendo: {[asignatura.nombre for asignatura in self.asignaturas]}"
    
    
class Estudiante(Persona):
    def __init__(self, nombre, dni, direccion, sexo, grado, curso_actual, creditos):
        super().__init__(nombre, dni, direccion, sexo) # el alumno toma los atributos de Persona
        self.grado = grado
        self.curso_actual = curso_actual
        self.creditos = creditos
        self.asignaturas = list()

    def matricularse_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def aprobar_asignatura(self, asignatura):
        if asignatura in self.asignaturas:
            self.creditos += asignatura.creditos
            self.asignaturas.remove(asignatura)

    def quitar_asignatura_aprobada(self, asignatura):
        if asignatura in self.asignaturas:
            self.asignaturas.remove(asignatura)
    
    def ganar_creditos(self, nuevos_creditos):
        self.creditos += nuevos_creditos
    
    def __str__(self):
        return super().__str__() + f"\nGrado:{self.grado}" + f"\nCurso:{self.curso_actual}" + f"\nAsignaturas matriculadas: {[asignatura.nombre for asignatura in self.asignaturas]}" + f"\nCreditos:{self.creditos}"

          
class Asignatura:
    def __init__(self, nombre, creditos, campo, dificultad):
        self.nombre = nombre
        self.creditos = creditos
        self.campo = campo
        self.dificultad = dificultad

    def __str__(self):
        return f"Nombre: {self.nombre} \nCreditos: {self.creditos} \nCampo: {self.campo} \nDificultad: {self.dificultad}"


class Universidad:
    def __init__(self):
        self.profesores = list()
        self.estudiantes = list()
        self.asignaturas = list()
    
    def añadir_profesores(self, *profesor): # Con * =>  desempaquetamos argumentos
        self.profesores.extend(profesor)

    def añadir_estudiantes(self, *estudiante):
        self.estudiantes.extend(estudiante)

    def añadir_asignaturas(self, *asignatura):
        self.asignaturas.extend(asignatura)

    def eliminar_profesores(self, *profesor):
        for p in profesor:
            if p in self.profesores:
                self.profesores.remove(p)

    def eliminar_estudiantes(self, *estudiante):
        for e in estudiante:
            if e in self.estudiantes:
                self.estudiantes.remove(e)
    
    def eliminar_asignaturas(self, *asignatura):
        for a in asignatura:
            if a in self.asignaturas:
                self.asignaturas.remove(a)
    
    def __str__(self):
        print()
        print(" ---- Universidad ---- ")

        imprimir = "Profesores: "
        for profesor in self.profesores:
            imprimir += profesor.nombre + '  '

        imprimir += "Estudiantes: "
        for estudiante in self.estudiantes:
            imprimir += estudiante.nombre + '  '
    
        imprimir += "Asignaturas: "
        for asignatura in self.asignaturas:
            imprimir += asignatura.nombre + '  '
        return imprimir


# Probamos el código:
if __name__ == "__main__":

    asignatura = Asignatura("Fisica", 6, "Ciencias Puras", "8")
    print(asignatura)
    print()

    investigador = ProfesorTitular("Enriqueta", "256234189L", "Perico Molino", "F", 96, 2, 200, 1, "Astronomía")
    investigador.nueva_asignatura(asignatura)
    investigador.obtener_departamento()
    print(investigador)
    print()

    estudiante = Estudiante("Mario", "256234189O", "Gato Mojado", "M", "Ingenieria Aeroespacial", 3, 72)
    print(estudiante)
    estudiante.ganar_creditos(6)
    estudiante.matricularse_asignatura(asignatura)
    print(estudiante)

    universidad = Universidad()
    universidad.añadir_profesores(investigador)
    universidad.añadir_estudiantes(estudiante)
    universidad.añadir_asignaturas(asignatura)
    print(universidad)
    universidad.eliminar_estudiantes(estudiante)
    print(universidad)
    universidad.añadir_estudiantes(estudiante)
    universidad.eliminar_asignaturas(asignatura)
    print(universidad)
  