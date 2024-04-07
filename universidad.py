"""
Implementación de un sistema de gestión universitario.
"""
# Importamos las librerías necesarias:
from enum import Enum
import pytest

class Persona:
    def __init__(self, nombre, dni, direccion, sexo):
        if isinstance(nombre, str):  # nos aseguramos de que el nombre sea una cadena
            self.nombre = nombre
        else:
            raise ValueError("El nombre no puede contener números de ningún tipo")
        self.dni = dni
        self.direccion = direccion
        self.sexo = sexo
    
    def __str__(self):  # función que imrpime los datos de una clase
        return f"Nombre: {self.nombre} \nDNI: {self.dni} \nDirección: {self.direccion} \nSexo: {self.sexo}"


class Departamento(Enum):  # esta clase será una enumeración de los diferentes departamentos existentes
    DIIC = 1
    DITEC = 2
    DIS = 3


class ProfesorDepartamentoError(Exception):  # en caso de que el departamento introducido no sea el correcto
    def listar_departamentos(self):
        print("Elije uno de los siguientes:")
        for d in Departamento:                # se recorre la clase Departamento y se imprimen las diferentes opciones al usuario
            print(f"{d.name}: {d.value}")

# Hay que colocar el error en Asignatura aquí porque Profesor hace uso de esta
class AsignaturaError(Exception):  # en caso de que la asignatura introducida no sea la correcta
    def listar_asignaturas():
            print("Las asignaturas disponibles son:")
            for asignatura in Asignatura:    # se recorre la clase Asignatura y se imprimen las diferentes opciones al usuario
                print(asignatura.nombre)


class Profesor(Persona):
    def __init__(self, nombre, dni, direccion, sexo, creditos, años_servicio, limite_creditos, departamento):
        super().__init__(nombre, dni, direccion, sexo) # profesor hereda los atributos de Persona

        if isinstance(creditos, int): # comprobamos que el crédito sea un número entero
            self.creditos = creditos
        else:
            raise ValueError("Un crédito tiene que ser un número entero") # lanzamos excepción
        
        if isinstance(limite_creditos, int):  # comprobamos que el límite también sea un número entero
            self.limite_creditos = limite_creditos
        else:
            raise ValueError("Un crédito tiene que ser un número entero") # lanzamos excepción
        
        self.años_servicio = años_servicio
        self.asignaturas = list()  # guardaremos todas las asignaturas en esta lista

        # Comprobamos que el departamento exista
        if not isinstance(departamento, Departamento):  # si no está en la clase, lanzaremos la excepción
            raise ProfesorDepartamentoError("Este departamento no existe")
        self.departamento = departamento
   

    def cambiar_departamento(self, otro_departamento):
        if isinstance(otro_departamento, Departamento): # comprobamos que otro_departamento esté en la clase Departamento
            self.departamento = otro_departamento  # este será el nuevo departamento
        else:
            raise ProfesorDepartamentoError("Debe existir el departamento") # de lo contrario lanzamos una excepción
    
    def obtener_departamento(self):
        return self.departamento  # devolvemos el departamento actual
    
    def ganar_creditos(self, nuevos_creditos):
        if isinstance(nuevos_creditos, int):  # comprobamos que sea un número entero
            self.creditos += nuevos_creditos  # sumamos al total de créditos
        else:
            raise ValueError("Un crédito tiene que ser un número entero") # si no lanzamos una excepción
    
    def nueva_asignatura(self, nueva_asignatura):
        if isinstance(nueva_asignatura, Asignatura):  # comprobamos que esté en la clase Asigantura
            self.asignaturas.append(nueva_asignatura)  # añadimos la nueva asignatura a la lista
        else:
            raise AsignaturaError("La asignatura debe estar en el catálogo")  # si no lanzamos una excepción

    def eliminar_asignatura(self, asignatura): 
        if asignatura in self.asignaturas:  # si la asignatura está en la lista la eliminamos
            self.asignaturas.remove(asignatura)


class ProfesorTitular(Profesor):
    def __init__(self, nombre, dni, direccion, sexo, creditos, años_servicio, limite_creditos, departamento, area_investigacion):
        super().__init__(nombre, dni, direccion, sexo, creditos, años_servicio, limite_creditos, departamento)
        self.tipo = "Profesor investigador"
        self.area_investigacion = area_investigacion
    
    def __str__(self):
        return super().__str__() + f"\nDepartamento: {self.departamento}" + f"\nAsignaturas impartiendo: {[asignatura.nombre for asignatura in self.asignaturas]}" + f"\nArea de Investigacion: {self.area_investigacion}"


class ProfesorAsociado(Profesor):
    def __init__(self, nombre, dni, direccion, sexo, creditos, años_servicio, limite_creditos, departamento, _trabajo_externo):
        super().__init__(nombre, dni, direccion, sexo, creditos, años_servicio, limite_creditos, departamento)
        self.trabajo_externo = _trabajo_externo  # el trabajo externo es un atributo privado

    def __str__(self):
        return super().__str__() + f"\nDepartamento: {self.departamento}" + f"\nAsignaturas impartiendo: {[asignatura.nombre for asignatura in self.asignaturas]}" # se imprime el nombre de cada asignatura en la lista
    



class Estudiante(Persona):
    def __init__(self, nombre, dni, direccion, sexo, grado, curso_actual, creditos):
        super().__init__(nombre, dni, direccion, sexo) # el alumno hereda los atributos de Persona

        if isinstance(grado, str): # El grado debe ser una cadena
            self.grado = grado
        else:
            raise ValueError("El grado no puede contener números de ningún tipo")
    
        if isinstance(creditos, int): # comprobamos que creditos sea un nº entero
            self.creditos = creditos
        else:
            raise ValueError("Un crédito tiene que ser un número entero")
        
        self.curso_actual = curso_actual
        self.asignaturas = list()  # guardaremos todas las asignaturas en esta lista


    def matricularse_asignatura(self, asignatura):
        if isinstance(asignatura, Asignatura):  # comprobamos que la asignatura introducida esté en la clase Asigantura
            self.asignaturas.append(asignatura) # si está la añadimos a la lista
        else:
            raise AsignaturaError("La asignatura debe estar en el catálogo") # de lo contrario lanzamos una excepción
        
    def aprobar_asignatura(self, asignatura):
        if asignatura in self.asignaturas:  # comprobamos que se haya matriculado anteriormente
            self.creditos += asignatura.creditos  # al aprobar la asignatura se le suman los créditos de ésta
            self.asignaturas.remove(asignatura)   # la eliminamos de la lista

    def quitar_asignatura(self, asignatura):
        if asignatura in self.asignaturas:   # comprobamos que se haya matriculado anteriormente
            self.asignaturas.remove(asignatura) # eliminamos la asignatura
    
    def ganar_creditos(self, nuevos_creditos):
        if isinstance(nuevos_creditos, int):  # comprobamos que sea un entero
            self.creditos += nuevos_creditos  # sumamos los créditos a los ya existentes
        else:
            raise ValueError("Un crédito tiene que ser un número entero") # si no es entero: excepción
    
    def __str__(self):
        return super().__str__() + f"\nGrado:{self.grado}" + f"\nCurso:{self.curso_actual}" + f"\nAsignaturas matriculadas: {[asignatura.nombre for asignatura in self.asignaturas]}" + f"\nCreditos:{self.creditos}"



class Asignatura:
    def __init__(self, nombre, creditos, campo, dificultad):
        if isinstance(nombre, str): # comprobamos que nombre sea una cadena
            self.nombre = nombre
        else:
            raise ValueError("El nombre no puede contener números de ningún tipo") # de lo contrario lanzamos una excepción
        
        if isinstance(creditos, int): # comprobamos que sea un entero
            self.creditos = creditos
        else:
            raise ValueError("Un crédito tiene que ser un número entero") # si no es entero: excepción
        
        self.campo = campo
        self.dificultad = dificultad

    def __str__(self):
        return f"Nombre: {self.nombre} \nCreditos: {self.creditos} \nCampo: {self.campo} \nDificultad: {self.dificultad}"


# Conjunto de posibles excepciones a lanzar para Universidad en caso de no encontrar una asignatura, profesor o estudiante
class ProfesorNoExisteException(Exception):
    def __init__(self, mensaje_error):
        self.message = mensaje_error # sólo imprimimos el mensaje de error
class EstudianteNoExisteException(Exception):
    def __init__(self, mensaje_error):
        self.message = mensaje_error
class AsignaturaNoExisteException(Exception):
    def __init__(self, mensaje_error):
        self.message = mensaje_error

class Universidad:
    def __init__(self):
        self.profesores = list() # tendremos una lista de los profesores, estudiantes y asignaturas en esta clase
        self.estudiantes = list()
        self.asignaturas = list()

    # Con * =>  desempaquetamos argumentos y podemos añadir más de uno a la vez

    def añadir_profesores(self, *profesor): # añadimos uno o más profesores creados (ProfesorTitular, ProfesorAsociado)
        self.profesores.extend(profesor)   # agregamos los profesores a la lista

    def añadir_estudiantes(self, *estudiante): # añadimos uno o más estudiantes creados (Estudiante)
        self.estudiantes.extend(estudiante)   # agregamos los profesores a la lista

    def añadir_asignaturas(self, *asignatura): # añadimos una o más asignaturas creadas (Asignatura)
        self.asignaturas.extend(asignatura)   # agregamos los profesores a la lista

    def eliminar_profesores(self, *profesor): # introducimos profesor\es
        for p in profesor:  # para cada profesor introducido
            if p in self.profesores:  # comprobamos que esxista en nuestra lista
                self.profesores.remove(p)  # lo eliminamos

    def eliminar_estudiantes(self, *estudiante): # introducimos estudiante\es
        for e in estudiante:  # para cada estudiante introducido
            if e in self.estudiantes: # comprobamos que esxista en nuestra lista
                self.estudiantes.remove(e) # lo eliminamos
    
    def eliminar_asignaturas(self, *asignatura):  # introducimos asignatura\s
        for a in asignatura:  # para cada asignatura introducida
            if a in self.asignaturas: # comprobamos que esxista en nuestra lista
                self.asignaturas.remove(a)  # la eliminamos
    
    def buscar_profesor(self, nombre_profesor): # introducimos el nombre del profesor
        for profesor in self.profesores:  # recorremos la lista
            if profesor.nombre == nombre_profesor:  # si el nombre introducido coincide con alguno en la lista (si está en la lista)
                return nombre_profesor  # devolvemos el nombre
        raise ProfesorNoExisteException(f"El profesor no existe en la base de datos") # si no lanzamos una excepción
    
    def buscar_estudiante(self, nombre_estudiante):  # introducimos el nombre del estudiante
        for estudiante in self.estudiantes: # recorremos la lista
            if estudiante.nombre == nombre_estudiante:  # si el nombre introducido coincide con alguno en la lista (si está en la lista)
                return nombre_estudiante  # devolvemos el nombre
        raise EstudianteNoExisteException(f"El estudiante no existe en la base de datos") # si no lanzamos una excepción
    
    def buscar_asignatura(self, nombre_asignatura):  # introducimos el nombre de la asignatura
        for asignatura in self.asignaturas:  # recorremos la lista
            if asignatura.nombre == nombre_asignatura:  # si el nombre introducido coincide con alguno en la lista (si está en la lista)
                return nombre_asignatura   # devolvemos el nombre
        raise AsignaturaNoExisteException(f"La asignatura no existe en la base de datos")  # si no lanzamos una excepción
    
    def __str__(self):  # imprimimos las listas
        print()
        print(" ---- Universidad ---- ")

        imprimir = "\nProfesores: "
        for profesor in self.profesores: # recorremos la lista e imprimimos el nombre de cada profesor uno por uno
            imprimir += profesor.nombre + ' '

        imprimir += "\nEstudiantes: "
        for estudiante in self.estudiantes: # recorremos la lista e imprimimos el nombre de cada estudiante uno por uno
            imprimir += estudiante.nombre + ' '
    
        imprimir += "\nAsignaturas: "
        for asignatura in self.asignaturas: # recorremos la lista e imprimimos el nombre de cada asignatura una por una
            imprimir += asignatura.nombre + ' '
        return imprimir  # devolvemos


# Probamos el código:
if __name__ == "__main__":

    try:
        asignatura1 = Asignatura("Fisica", 6, "Ciencias Puras", "8") # La dificultad también podría expresarse como 'Media' o 'Fácil' en vez de un número
        asignatura2 = Asignatura("Biologia", 6, "Ciencias Puras", "7")
        print(asignatura1,'\n', asignatura2)
        print()

        DIS = Departamento.DIS
        investigador = ProfesorTitular("Enriqueta", "256234189L", "Perico Molino", "F", 96, 2, 200, DIS, "Astronomía")
        investigador.nueva_asignatura(asignatura1)
        obtener_departamento = investigador.obtener_departamento()
        print('Obtenemos departamento: ', obtener_departamento)
        externo = ProfesorAsociado("Enrique", "256290189L", "Perico Palote", "M", 112, 3, 200, DIS, "Carlitos S.L.")
        externo.nueva_asignatura(asignatura2)
        print(externo, '\n')
        print(investigador)

        print()

        estudiante = Estudiante("Mario", "256234189O", "Gato Mojado", "M", "Ingenieria Aeroespacial", 3, 72)
        estudiante.matricularse_asignatura(asignatura1)
        estudiante.matricularse_asignatura(asignatura2)
        estudiante.aprobar_asignatura(asignatura2)
        estudiante.ganar_creditos(6)
        print(estudiante)

        universidad = Universidad()
        universidad.añadir_profesores(investigador, externo)
        universidad.añadir_estudiantes(estudiante)
        universidad.añadir_asignaturas(asignatura1, asignatura2)
        print(universidad, '\n')
        universidad.eliminar_asignaturas(asignatura1)
        print(universidad)
        print()
        buscar_prof = universidad.buscar_profesor('Enrique')
        buscar_estudiante = universidad.buscar_estudiante('Mario')
        print(buscar_prof, buscar_estudiante)

    except (ProfesorDepartamentoError, AsignaturaError) as e: # si se dan los errores siguientes se ejecutarán las excepciones y se listarán las opciones al usuario
        e.listar_departamentos()
        e.listar_asignaturas()


    

# Hacemos tests:

# Clase Persona
def test_nueva_persona(): # Comprobamos si se imprime todo correctamente: debería pasar el test
    persona = Persona("Lola", "45474912Ñ", "Calle de los Golondrinos", "F")
    assert str(persona) == "Nombre: Lola \nDNI: 45474912Ñ \nDirección: Calle de los Golondrinos \nSexo: F"

# Clase Profesor
def test_cambiar_departamento(): # Comprobamos si el cambio de departamento funciona: debería pasar el test
    profesor = ProfesorTitular("Pascual", "32353954L", "Calle de las Ciencias", "M", 58, 3, 300, Departamento.DIS, 'Neurologia')
    assert profesor.departamento == Departamento.DIS
    profesor.cambiar_departamento(Departamento.DITEC)
    assert profesor.obtener_departamento()

def test_departamento_error():
    with pytest.raises(ProfesorDepartamentoError): # Test FALLIDO, probamos si la detección de departamento erróneo funciona
        ProfesorAsociado("Enrique", "256290189L", "Perico Palote", "M", 112, 3, 200, Departamento.YUC, "Carlitos S.L.")


# Clase Estudiante
def test_matricula_asignatura_estudiante(): #  Comprobamos si la función de matricularse en una asignatura funciona: debería pasar el test
    estudiante = Estudiante("Josefa", "65874262J", "Pollito Frito", "F", "GCID", 1, 0)
    asignatura = Asignatura("Programacion", 6, "Teleco", 5)
    estudiante.matricularse_asignatura(asignatura)
    assert asignatura in estudiante.asignaturas

def test_aprobar_asignatura(): # Comprobamos si la función de aprobar una asignatura funciona: debería pasar el test
    estudiante = Estudiante("Maria", "253784189O", "Gato Mojado", "F", "Ingenieria Aeroespacial", 3, 72)
    asignatura = Asignatura("Redes", 6, "Telocomunicaciones", 8)
    estudiante.matricularse_asignatura(asignatura)
    estudiante.aprobar_asignatura(asignatura)
    assert estudiante.creditos == 78 # al aprobar deben añadirse los 6 créditos
    assert asignatura not in estudiante.asignaturas


# Clase Asignatura
def test_nueva_asignatura():  # Haremos ahora un test FALLIDO, añadiendo una asignatura y comprobando si guarda bien el nombre o lo confunde con el campo
    asignatura = Asignatura("Redes", 6, "Telocomunicaciones", 8)
    assert asignatura.nombre == "Telocomunicaciones"
    assert asignatura.creditos == 6


# Clase Universidad
def test_nuevo_profesor_universidad(): # Comprobamos que un profesor se añada corretamente: debería pasar el test
    universidad = Universidad()
    profesor = ProfesorTitular("Pascual", "32353954L", "Calle de las Ciencias", "M", 58, 3, 300, Departamento.DIIC, 'Neurologia')
    universidad.añadir_profesores(profesor)
    assert profesor in universidad.profesores

def test_alumno_inventado(): # Test FALLIDO en el que comprobamos que la función de búsqueda de estudiantes funcione correctamente
    universidad = Universidad()
    estudiante1 = Estudiante("Mario", "256234189O", "Gato Mojado", "M", "Ingenieria Aeroespacial", 3, 72)
    estudiante2 = Estudiante("Maria", "253784189O", "Gato Mojado", "F", "Ingenieria Aeroespacial", 3, 78)
    universidad.añadir_estudiantes(estudiante1, estudiante2)
    assert universidad.buscar_estudiante("Lucas")

if __name__ == "__main__":
    pytest.main([__file__])  # ¡Comprobamos que todos los tests han dado el resultado que se esperaba! :)