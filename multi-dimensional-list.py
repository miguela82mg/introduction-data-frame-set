# Listas multidimensionales

# 1. Array o Lista
# Esto no es más que una matriz que almacena todos normalmente similares.
# Para este ejemplo vamos a escoger un listado de 10 países de Latinoamérica:

lat_Countries = ['Colombia', 'Argentina', 'Peru', 'Chile']
print("Listado de países en Latinoamérica: " + str(sorted(lat_Countries)))

# 2. Array o Lista bidimensional
# Bien, iniciemos con lo básico. Creemos un array o listado con ciudades que pertenezcan
# a los países mencionados anteriormente:

lat_Cities = [
    ['Bogota', 'Cali', 'Medellin'],
    ['Buenos Aires', 'Rosario', 'Mar del plata'],
    ['Lima', 'Curso', 'Trujillo'],
    ['Santiago de chile', 'La Serena', 'Temuco']
]

print("Ciudades que pertenecen a países latinos: " + str(sorted(lat_Cities)))

# Hasta este punto, todo es color de rosa. Definimos un array o lista bidimensional cuento encontramos
# un listado dentro de otro.
# Nota que aunque están las ciudades, no tenemos la relación entre estas y sus países. (Ya vamos a explicarlo)

# 3. Array o lista multidimensional
# Okay, ahora vamos a crear 2 colegios para cada ciudad, para cada país:

lat_school = [
    [
        ['Colegio 1', 'Colegio 2'],
        ['Colegio 1', 'Colegio 2'],
        ['Colegio 1', 'Colegio 2'],
    ],
    [
        ['Colegio 1', 'Colegio 2'],
        ['Colegio 1', 'Colegio 2'],
        ['Colegio 1', 'Colegio 2'],
    ],
    [
        ['Colegio 1', 'Colegio 2'],
        ['Colegio 1', 'Colegio 2'],
        ['Colegio 1', 'Colegio 2'],
    ],
    [
        ['Colegio 1', 'Colegio 2'],
        ['Colegio 1', 'Colegio 2'],
        ['Colegio 1', 'Colegio 2'],
    ]
]

print("Colegios que pertenecen a ciudades en países latinos: " +
      str(sorted(lat_school)))

# Perfecto. No te pierdas, vamos a dejarlo aquí, Esto es un que en su interior tiene dos listados
# de nivel adicionales.
# Es necesario entender este concepto para el análisis de datos.

# 3. Dataset
#  Ahora vamos a darle forma a esta estructura para que se nos haga más familiar:

lat_setSchool = [
    {
        "pais": "Colombia",
        "ciudades": [
            {
                "ciudad": "Bogota",
                "colegios": ['Colegio 1', 'Colegio 2']
            },
            {
                "ciudad": "Cali",
                "colegios": ['Colegio 1', 'Colegio 2']
            },
            {
                "ciudad": "Medellin",
                "colegios": ['Colegio 1', 'Colegio 2']
            }
        ]
    },
    {
        "pais": "Argentina",
        "ciudades": [
            {
                "ciudad": "Buenos Aires",
                "colegios": ['Colegio 1', 'Colegio 2']
            },
            {
                "ciudad": "Rosario",
                "colegios": ['Colegio 1', 'Colegio 2']
            },
            {
                "ciudad": "Mar del plata",
                "colegios": ['Colegio 1', 'Colegio 2']
            }
        ]
    },
    {
        "pais": "Peru",
        "ciudades": [
            {
                "ciudad": "Lima",
                "colegios": ['Colegio 1', 'Colegio 2']
            },
            {
                "ciudad": "Curso",
                "colegios": ['Colegio 1', 'Colegio 2']
            },
            {
                "ciudad": "Trujillo",
                "colegios": ['Colegio 1', 'Colegio 2']
            }
        ]
    },
    {
        "pais": "Chile",
        "ciudades": [
            {
                "ciudad": "Santiago de chile",
                "colegios": ['Colegio 1', 'Colegio 2']
            },
            {
                "ciudad": "La Serena",
                "colegios": ['Colegio 1', 'Colegio 2']
            },
            {
                "ciudad": "Temuco",
                "colegios": ['Colegio 1', 'Colegio 2']
            }
        ]
    },
]

print("Data set de colegios: " + str(lat_setSchool))

# De seguro que esta estructura si se te hace familiar.
# Esto se conoce como dataset, es probable que si observas el código de una tabla en SQL, o la estructura NOSQL
# de una base de datos mongo, firebase o cualquiera, observes algo similar.

# Revisa dataset-dataframe para continuar
