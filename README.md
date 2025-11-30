# Práctica 3.4: JSON y XML

---

# Índice
1. [Identificación de la Actividad](#identificación-de-la-actividad)
2. [Descripción de la Actividad](#descripción-de-la-actividad)
3. [Instrucciones de Compilación y Ejecución](#instrucciones-de-compilación-y-ejecución)
4. [Ejemplos de Ejecución](#ejemplos-de-ejecución)
5. [Programas Desarrollados](#programas-desarrollados)
6. [Desarrollo de la Actividad](#desarrollo-de-la-actividad)
7. [Resultados de Pruebas](#resultados-de-pruebas)
8. [Documentación Adicional](#documentación-adicional)
9. [Conclusiones](#conclusiones)
10. [Referencias y Fuentes](#referencias-y-fuentes)

## Identificación de la Actividad
- **ID de la Actividad:** PRO_3_4_ALG
- **Módulo:** Programación (PROG)
- **Unidad de Trabajo:** 3.4 - Estructuras de datos: JSON y XML
- **Fecha de Creación:** 27/11/25
- **Fecha de Entrega:** 30/11/25
- **Alumno(s):** 
  - **Nombre y Apellidos:** Antonio López Gautier
  - **Correo electrónico:** alopgau418@g.educaand.es
  - **Iniciales del Alumno/Grupo:** ALG

## Descripción de la Actividad
Esta práctica consiste en la implementación de programas en Python para trabajar con formatos JSON y XML. Incluye operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre datos estructurados, conversión entre formatos JSON y XML, y pruebas unitarias para validar la funcionalidad. Los programas demuestran el manejo de datos estructurados usando las bibliotecas estándar de Python.

## Instrucciones de Compilación y Ejecución
1. **Requisitos Previos:**
   - Python 3.6 o superior
   - No se requieren dependencias externas

2. **Pasos para Ejecutar el Código:**
   ```bash
   # Ejecutar programas principales
   python src/main_json.py
   python src/main_xml.py
   python src/convertidor.py
   
   # Ejecutar pruebas unitarias
   pytest tests/test_json.py -v
   pytest tests/test_xml.py -v
   ```

## Ejemplos de Ejecución

### main_json.py
```bash
Datos inicializados desde 'datos_usuarios_orig.json' a 'datos_usuarios.json'.
---Contenido actual del JSON---
ID: 1 Nombre: Ana Edad: 25 
---Fin del contenido---
Presione Enter para continuar
Actualizada la edad del usuario con id 1
---Contenido actual del JSON---
ID: 1 Nombre: Ana Edad: 26 
---Fin del contenido---
```

### main_xml.py
```bash
Datos inicializados desde 'datos_usuarios_orig.xml' a 'datos_usuarios.xml'.
---Contenido actual del XML---
ID: 1 Nombre: Ana Edad: 25 
---Fin del contenido---
Presione Enter para continuar
Actualizada la edad del usuario con id 1
---Contenido actual del XML---
ID: 1 Nombre: Ana Edad: 31 
---Fin del contenido---
```

### convertidor.py
```bash
# Convierte datos entre formatos JSON y XML automáticamente
# Genera archivos: datos_convertidor_orig.json, datos_convertidor.xml, datos_convertidor.json
```

## Programas Desarrollados

### [main_json.py](src/main_json.py)
Sistema de gestión de datos en formato JSON que incluye:
- Carga y visualización de datos de usuarios
- Actualización de edades
- Inserción de nuevos usuarios
- Eliminación de usuarios existentes
- Validación de archivos y manejo de errores

### [main_xml.py](src/main_xml.py)
Sistema de gestión de datos en formato XML que incluye:
- Parseo y manipulación de documentos XML
- Operaciones CRUD sobre datos estructurados
- Creación de árboles XML dinámicamente
- Manejo de excepciones específicas de XML

### [convertidor.py](src/convertidor.py)
Conversor entre formatos JSON y XML:
- Conversión bidireccional JSON ↔ XML
- Mantenimiento de la estructura de datos
- Generación de archivos de salida formateados

## Desarrollo de la Actividad

### Descripción del Desarrollo
Se han desarrollado 3 programas principales que implementan operaciones CRUD sobre datos estructurados en formatos JSON y XML. Cada programa incluye:

- Funciones modulares con tipado de datos
- Validación robusta de archivos de entrada
- Manejo de excepciones específicas por formato
- Interfaz de usuario clara mediante consola
- Pruebas unitarias exhaustivas

### Estructura del Proyecto
```
├── src/
│   ├── main_json.py      # Gestor de datos JSON
│   ├── main_xml.py       # Gestor de datos XML  
│   └── convertidor.py    # Conversor JSON/XML
├── tests/
│   ├── test_json.py      # Pruebas para JSON
│   └── test_xml.py       # Pruebas para XML
└── README.md
```

### Funcionalidades Implementadas

#### Operaciones CRUD
- **Crear:** Inserción de nuevos usuarios con IDs automáticos
- **Leer:** Visualización de todos los usuarios en formato estructurado
- **Actualizar:** Modificación de edades de usuarios existentes
- **Eliminar:** Remoción de usuarios específicos por ID

#### Conversión de Formatos
- JSON → XML: Conversión completa manteniendo la estructura anidada
- XML → JSON: Parseo y transformación a diccionarios Python
- Validación de integridad de datos durante la conversión

## Resultados de Pruebas

### Pruebas para JSON
```bash
pytest tests/test_json.py -v
```
```text
tests/test_json.py::test_actualizar_edad[archivo_inicial0-esperado_edad0] PASSED
tests/test_json.py::test_actualizar_edad[archivo_inicial1-esperado_edad1] PASSED
tests/test_json.py::test_insertar_usuario[archivo_inicial0-esperado_ids0] PASSED
tests/test_json.py::test_insertar_usuario[archivo_inicial1-esperado_ids1] PASSED
tests/test_json.py::test_eliminar_usuario[archivo_inicial0-esperado_ids0] PASSED
tests/test_json.py::test_eliminar_usuario[archivo_inicial1-esperado_ids1] PASSED
```

### Pruebas para XML
```bash
pytest tests/test_xml.py -v
```
```text
tests/test_xml.py::test_actualizar_edad[usuarios_inicial0-edad_esperada0] PASSED
tests/test_xml.py::test_actualizar_edad[usuarios_inicial1-edad_esperada1] PASSED
tests/test_xml.py::test_insertar_usuario[usuarios_inicial0-ids_esperados0] PASSED
tests/test_xml.py::test_insertar_usuario[usuarios_inicial1-ids_esperados1] PASSED
tests/test_xml.py::test_eliminar_usuario[usuarios_inicial0-ids_esperados0] PASSED
tests/test_xml.py::test_eliminar_usuario[usuarios_inicial1-ids_esperados1] PASSED
```

### Pruebas para Convertidor
```bash
pytest tests/test_convertidor.py -v
```
```text
tests/test_convertidor.py::test_json_inicial[datos0] PASSED
tests/test_convertidor.py::test_json_inicial[datos1] PASSED
tests/test_convertidor.py::test_json_a_xml[entrada0-esperado_tags0] PASSED
tests/test_convertidor.py::test_json_a_xml[entrada1-esperado_tags1] PASSED
tests/test_convertidor.py::test_xml_a_json[xml_contenido0-esperado_json0] PASSED
tests/test_convertidor.py::test_xml_a_json[xml_contenido1-esperado_json1] PASSED
```
## Documentación Adicional

### Archivos de Configuración
- **datos_usuarios_orig.json**: Datos de ejemplo en formato JSON
- **datos_usuarios_orig.xml**: Datos de ejemplo en formato XML
- **datos_usuarios.json**: Archivo de trabajo JSON (se genera automáticamente)
- **datos_usuarios.xml**: Archivo de trabajo XML (se genera automáticamente)

### Características Técnicas
- Uso de `json` y `xml.etree.ElementTree` de la biblioteca estándar
- Validación de integridad de archivos
- Manejo de errores con mensajes descriptivos
- Código modular y reutilizable
- Pruebas unitarias parametrizadas

## Conclusiones
Esta práctica ha demostrado la importancia de los formatos JSON y XML en el manejo de datos estructurados. Se han implementado operaciones CRUD completas en ambos formatos, mostrando las diferencias en el manejo de cada uno. La conversión entre formatos permite la interoperabilidad entre sistemas, mientras que las pruebas unitarias garantizan la robustez del código.

## Referencias y Fuentes
- [Documentación oficial de Python: JSON](https://docs.python.org/3/library/json.html)
- [Documentación oficial de Python: XML](https://docs.python.org/3/library/xml.etree.elementtree.html)
- [Práctica JSON - ReviloFE](https://revilofe.github.io/section1/u03/practica/PROG-U3.-Practica004/)
- [Práctica XML - ReviloFE](https://revilofe.github.io/section1/u03/practica/PROG-U3.-Practica005/)

### Notas Adicionales:
- **Nombres de Archivos:** Cada programa sigue la nomenclatura estándar del proyecto
- **Independencia:** Los programas pueden ejecutarse de forma independiente
- **Compatibilidad:** El código es compatible con Python 3.6+
- **Manejo de Errores:** Todos los programas incluyen validación robusta de archivos
- **Pruebas:** Cobertura completa con pytest para todas las funcionalidades