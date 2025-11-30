
import xml.etree.ElementTree as ET
from main_json import espera, limpiar_consola
def cargar_xml(destino:str) -> ET.ElementTree:
    """Carga el XML origen y lo convierte a árbol
    Args:
        nombre_fichero (str): Nombre del archivo XML
    Returns:
        ET.ElementTree: Árbol del XML
    """
    try:
        origen = ET.parse("datos_usuarios_orig.xml")
    except (FileNotFoundError,ET.ParseError):
        crear_arbol("usuarios")
    else:
        origen.write(destino, encoding="utf-8", xml_declaration=True)
        return ET.parse(destino)


def mostrar_datos(archivo:ET.ElementTree) -> bool:
    """Muestra los datos del XML en consola
    Args:
        archivo (ET.ElementTree): archivo XML

    Returns:
        False: Hay algún error
        True: No hay errores

    """

    raiz = archivo.getroot()
    if len(raiz.findall("usuario")) == 0:
        print("No hay usuarios listados")
        return False
    else:
        print("---Contenido actual del XML---")
        for usuario in raiz.findall("usuario"):
            print(f"ID: {usuario.find("id").text} Nombre: {usuario.find("nombre").text} Edad: {usuario.find("edad").text} ")
        print("---Fin del contenido---")
        return True
def crear_arbol(str_raiz:str) -> None:
        """ Genera un XML con dicha raiz
            Args:
                str_raiz (str): Nodo raiz
            Returns:
                None
            """
        raiz = ET.Element(str_raiz)
        arbol_nuevo = ET.ElementTree(raiz)
        arbol_nuevo.write("datos_usuarios.xml", encoding="utf-8", xml_declaration=True)

def inicializar_datos(origen:str) -> bool:
    """Comprueba si hay algún error en el archivo
    Returns:
        False: Hay algún error
        True: No hay errores
    """
    try:
        arbol = ET.parse(origen)
    except FileNotFoundError:
        print(f" El archivo {origen} no existe Asegurate que esté en el directorio raiz.")
        return False

    except ET.ParseError:
        print("El archivo XML tiene un formato incorrecto.")
        return False
    else:
        print(f"Datos inicializados desde '{origen}' a 'datos_usuarios.xml'.")
        return True
def actualizar_edad(archivo:ET.ElementTree) -> None:
    """Actualiza la edad de un usuario
    Args:
        archivo (ET.ElementTree): archivo entrante
    Returns:
        None"""
    archivo.find("usuario").find("edad").text = "31"
    print("Actualizada la edad del usuario con id 1")

def insertar_usuario(archivo:ET.ElementTree) -> None:
    """Inserta un usuario
        Args:
            archivo (ET.ElementTree): archivo entrante
        Returns:
            None"""
    raiz = archivo.getroot()
    usuario = ET.SubElement(raiz,"usuario")
    ET.SubElement(usuario,"id").text = "3"
    ET.SubElement(usuario,"nombre").text = "Pedro"
    ET.SubElement(usuario,"edad").text = "40"

    print("Usuario Pedro añadido con éxito")
def eliminar_usuario(archivo:ET.ElementTree) -> None:
    """Elimina un usuario
            Args:
                archivo (ET.ElementTree): archivo entrante
            Returns:
                None"""
    raiz = archivo.getroot()
    for usuario in raiz.findall("usuario"):
        if usuario.find("id").text == "2":
            raiz.remove(usuario)
    print("Usuario con ID 2 eliminado")
def actualizar_archivo(archivo:ET.ElementTree) -> None:
    """Actualiza el XML
               Args:
                   archivo (ET.ElementTree): archivo entrante
               Returns:
                   None"""
    archivo.write("datos_usuarios.xml", encoding="utf-8", xml_declaration=True)
    print("Archivo actualizado correctamente")



def main():
    if inicializar_datos("datos_usuarios_orig.xml"):
        archivo = cargar_xml("datos_usuarios.xml")
        if mostrar_datos(archivo):
            espera()
            limpiar_consola()
            actualizar_edad(archivo)
            mostrar_datos(archivo)
            espera()
            limpiar_consola()
            insertar_usuario(archivo)
            mostrar_datos(archivo)
            espera()
            limpiar_consola()
            eliminar_usuario(archivo)
            mostrar_datos(archivo)
            espera()
            actualizar_archivo(archivo)



if __name__ == "__main__":
    main()