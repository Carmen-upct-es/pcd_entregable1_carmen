"""
Implementación de un sistema de gestión universitario.
"""

from enum import Enum
import pytest

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


class ProfesorDepartamentoError(Exception):
    def listar_departamentos(self):
        print("Elije uno de los siguientes:")
        for d in Departamento:
            print(f"{d.name}: {d.value}")

# Hay que colocar el error en Asignatura aquí porque Profesor hace uso de esta
class AsignaturaError(Exception):
    def listar_asignaturas():
            print("Las asignaturas disponibles son:")
            for asignatura in Asignatura:
                print(asignatura.nombre)

class Profesor(Persona):
    def __init__(self, nombre, dni, direccion, sexo, creditos, años_servicio, limite_creditos, departamento):
        super().__init__(nombre, dni, direccion, sexo) # profesor toma los atributos de Persona
        self.creditos = creditos
        self.años_servicio = años_servicio
        self.limite_creditos = limite_creditos
        self.asignaturas = list()
        if not isinstance(departamento, Departamento):
            raise ProfesorDepartamentoError("El departamento no existe")
        self.departamento = departamento
   
    def cambiar_departamento(self, otro_departamento):
        if isinstance(otro_departamento, Departamento): # comprobamos que otro_departamento esté en la clase Departamento
            self.departamento = otro_departamento
        else:
            raise ProfesorDepartamentoError("Debe existir el departamento") # si no lanzamos una excepción
    
    def obtener_departamento(self):
        if isinstance(self.departamento, Departamento):
            return self.departamento
    
    def ganar_creditos(self, nuevos_creditos):
        if isinstance(nuevos_creditos, int):    # comprobamos que sea un nº entero, si no ponemos isinstance(if nuevos_creditos is int), dará error porque no es int
            self.creditos += nuevos_creditos
        else:
            raise ValueError("Un crédito debe ser un número entero") # si no lanzamos una excepción
    
    def nueva_asignatura(self, nueva_asignatura):
        if isinstance(nueva_asignatura, Asignatura):  # comprobamos que esté en la clase Asigantura
            self.asignaturas.append(nueva_asignatura)
        else:
            raise AsignaturaError("La asignatura debe estar en el catálogo")  # si no lanzamos una excepción

    def eliminar_asignatura(self, asignatura):
        if isinstance(asignatura, Asignatura):
            self.asignaturas.remove(asignatura)
        else:
            raise AsignaturaError("La asignatura debe estar en el catálogo")


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
        if isinstance(asignatura, Asignatura):  # comprobamos que esté en la clase Asigantura
            self.asignaturas.append(asignatura)
        else:
            raise AsignaturaError("La asignatura debe estar en el catálogo") # lanzar excepción
        
    def aprobar_asignatura(self, asignatura):
        if asignatura in self.asignaturas:  # comprobamos que se haya matriculado anteriormente
            self.creditos += asignatura.creditos
            self.asignaturas.remove(asignatura)

    def quitar_asignatura_aprobada(self, asignatura):
        if asignatura in self.asignaturas:   # comprobamos que se haya matriculado anteriormente
            self.asignaturas.remove(asignatura)
    
    def ganar_creditos(self, nuevos_creditos):
        if isinstance(nuevos_creditos, int):   # comprobamos que sea un nº entero, si no ponemos isinstance(if nuevos_creditos is int), dará error porque no es int
            self.creditos += nuevos_creditos
        else:
            raise ValueError("Un crédito debe ser un número entero") # lanzamos excepción
    
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


class ProfesorNoExisteException(Exception):
    def __init__(self, mensaje_error):
        self.message = mensaje_error
class EstudianteNoExisteException(Exception):
    def __init__(self, mensaje_error):
        self.message = mensaje_error
class AsignaturaNoExisteException(Exception):
    def __init__(self, mensaje_error):
        self.message = mensaje_error

class Universidad:
    def __init__(self):
        self.profesores = list()
        self.estudiantes = list()
        self.asignaturas = list()
    
    def añadir_profesores(self, *profesor): # Con * =>  desempaquetamos argumentos (podemos añadir más de uno)
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
    
    def buscar_profesor(self, nombre_profesor):
        for profesor in self.profesores:
            if profesor.nombre == nombre_profesor:
                return nombre_profesor
        raise ProfesorNoExisteException(f"El profesor no existe en la base de datos")
    
    def buscar_estudiante(self, nombre_estudiante):
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre_estudiante:
                return nombre_estudiante
        raise EstudianteNoExisteException(f"El estudiante no existe en la base de datos")
    
    def buscar_asignatura(self, nombre_asignatura):
        for asignatura in self.asignaturas:
            if asignatura.nombre == nombre_asignatura:
                return nombre_asignatura
        raise AsignaturaNoExisteException(f"La asignatura no existe en la base de datos")
    
    def __str__(self):
        print()
        print(" ---- Universidad ---- ")

        imprimir = "\nProfesores: "
        for profesor in self.profesores:
            imprimir += profesor.nombre + ' '

        imprimir += "\nEstudiantes: "
        for estudiante in self.estudiantes:
            imprimir += estudiante.nombre + ' '
    
        imprimir += "\nAsignaturas: "
        for asignatura in self.asignaturas:
            imprimir += asignatura.nombre + ' '
        return imprimir


# Probamos el código:
if __name__ == "__main__":

    try:
        asignatura = Asignatura("Fisica", 6, "Ciencias Puras", "8")
        print(asignatura)
        print()

        DIS = Departamento.DIS
        investigador = ProfesorTitular("Enriqueta", "256234189L", "Perico Molino", "F", 96, 2, 200, DIS, "Astronomía")
        investigador.nueva_asignatura(asignatura)
        investigador.obtener_departamento()
        print(investigador)
        externo = ProfesorAsociado("Enrique", "256290189L", "Perico Palote", "M", 112, 3, 200, DIS, "Carlitos S.L.")
        print(externo)
        print()

        estudiante = Estudiante("Mario", "256234189O", "Gato Mojado", "M", "Ingenieria Aeroespacial", 3, 72)
        print(estudiante)
        estudiante.ganar_creditos(6)
        estudiante.matricularse_asignatura(asignatura)
        print(estudiante)

        universidad = Universidad()
        universidad.añadir_profesores(externo)
        universidad.añadir_estudiantes(estudiante)
        universidad.añadir_asignaturas(asignatura)
        print(universidad)
        universidad.eliminar_estudiantes(estudiante)
        print(universidad)
        universidad.añadir_estudiantes(estudiante)
        universidad.eliminar_asignaturas(asignatura)
        print(universidad)
        print()
        buscar_prof = universidad.buscar_profesor('Enrique')
        buscar_estudiante = universidad.buscar_estudiante('Mario')
        print(buscar_prof, buscar_estudiante)

    except (ProfesorDepartamentoError, AsignaturaError) as e:
        e.listar_departamentos()
        e.listar_asignaturas()


    

# Hacemos tests:
    
def test_nueva_persona():
    persona = Persona("Lola", "45474912Ñ", "Calle de los Golondrinos", "F")
    assert str(persona) == 'Nombre: Lola \nDNI: 45474912Ñ \nDirección: Calle de los Golondrinos \nSexo: F'

def test_contratar_profesor():
    profesor = Profesor("Pascual", "32353954L", "Calle de las Ciencias", "M", 58, 3, 300, Departamento.DIS)
    assert profesor.departamento == Departamento.DIS
    profesor.cambiar_departamento(Departamento.DITEC)
    assert profesor.obtener_departamento

def test_matricula_asignatura_estudiante():
    estudiante = Estudiante("Josefa", "65874262J", "Pollito Frito", "F", "GCID", 1, 0)
    asignatura = Asignatura("Programacion", 6, "Teleco", 5)
    estudiante.matricularse_asignatura(asignatura)
    assert asignatura in estudiante.asignaturas

def test_nueva_asignatura():  # Haremos ahora un test FALLIDO a posta, añadiendo una asignatura y comprobando si guarda bien el nombre o lo confunde con el campo
    asignatura = Asignatura("Redes", 6, "Telocomunicaciones", 8)
    assert asignatura.nombre == "Telocomunicaciones"
    assert asignatura.creditos == 6

def test_nuevo_profesor_universidad():
    universidad = Universidad()
    profesor = Profesor("Pascual", "32353954L", "Calle de las Ciencias", "M", 58, 3, 300, Departamento.DIIC)
    universidad.añadir_profesores(profesor)
    assert profesor in universidad.profesores

if __name__ == "__main__":
    pytest.main([__file__])  # ¡Comprobamos que todos los tests han dado el resultado que se esperaba! :)