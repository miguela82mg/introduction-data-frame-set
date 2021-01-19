# Un dataframe se caracteriza por tener datos organizados en forma de array o Listas
# los cuales son fácilmente analizables. Y son los recomendados a la hora de procesar datos.
# A continuación te voy a mencionar algunas cosas que debes tener en cuenta:

# 1. Datos constantes
# Sin importar la finalidad del proyecto, análisis, automatización, ML, etc..
# Debes saber que todos los campos de tu dataset inicial deben estar definidos. Debes tener esto en cuenta
# principalmente si tus datos vienen de una base de datos NOSQL. Ya que si en algún frame, se escapa un campo
# o el valor de un campo se encuentra indefinido, el resultado no será fiable o podrás tener errores al procesar

# Ejemplo
# Supongamos que tenemos 3 colegios

school = [
    {
        "colegio": "Colegio1",
        "estudiantes": 76,
        "hombres": 16,
        "mujeres": undefined,
        "graduados": 18
    },
    {
        "colegio": "Colegio2",
        "estudiantes": 76,
        "hombres": 16,
        "mujeres": 60,
        # "graduados": 18
    },
    {
        "colegio": "Colegio3",
        "estudiantes": 76,
        "hombres": 16,
        "mujeres": 60,
        "graduados": 18
    }
]

# Si estos colegios pertenecen a la ciudad de Bogotá y se te es solicitado calcular
#  el total de graduados, rendimiento académico, porcentaje de hombres y mujeres estudiantes en la ciudad.
#  El no contar con el valor de un campo te dará dolores de cabeza.
#  Entonces intenta siempre tener valores definidos y operables, o por lo menos no tener ausencias
#  en los campos. (PELIGRO EN NOSQL)

#  2. Porque dataframe
# Bueno, el procesamiento de datos se utiliza generalmente para encontrar tendencias, ya sea Para
# luego ser utilizada en I.A. para predicciones, o explicar la razón de algunos hechos comerciales,
# económicos, sociales etc...

# En conclusión, la ciencia de datos no se utiliza para hacer consultas en valor de campos de bases de datos
# por ejemplo

school_Set = [
    {
        "colegio": "Colegio1",
        "estudiantes": 76,
        "hombres": 16,
        "mujeres": 60,
        "graduados": 18
    },
    {
        "colegio": "Colegio2",
        "estudiantes": 45,
        "hombres": 15,
        "mujeres": 30,
        "graduados": 20
    },
    {
        "colegio": "Colegio3",
        "estudiantes": 30,
        "hombres": 15,
        "mujeres": 15,
        "graduados": 30
    }
]

# ¿Cuantos graduados tiene el colegio3?
# No necesitas ser un experto en análisis para hacer una consulta con javascript y mostrarla al usuario

# Pero ¿En promedio cuantos estudiantes se gradúan?
# Bueno, aquí tampoco, pero puedes crear una función que sume un par de campos y luego los divida.
# Esto lo puedes hacer desde un front o un back según el tamaño de los datos, pero no será necesaria
# quemar demasiadas pestañas.

# ¿Cuál es promedio de hombre que se gradúan? ;)
# Que piensas de esta ¿si tuvieras estos mismos datos de los colegios de tu país,
# como sacarías este promedio?

# Bien aquí entra el poder de los algoritmos y la forma en que limpias los datos

# A. Refinas
# Dale a tú algoritmos solo lo que debes encontrar, por ahora el nombre colegio y el número de
# estudiantes (este lo puede sacar tu algoritmo) no será necesaria.

graduados = [18, 20, 30]
boys = [16, 15, 15]
girls = [60, 30, 15]

# Si entregas los datos correctos y tu algoritmo es el indicado, el resultado será más preciso.
# Ten en cuenta que existen muchas librerias que te ayudaran con todo esto.