import json
import os
def cargar_json(ruta_origen:str) -> None:
    """Carga el JSON de destino
    Args:
        ruta_origen (str): Ruta del archivo origen
    Returns:
        None
    """
    with open(ruta_origen, "r") as o:
        origen = json.load(o)

    with open("datos_usuarios.json", "w") as destino:
        json.dump(origen,destino, indent=4)

    with open("datos_usuarios.json", "r") as destino:
        archivo = json.load(destino)
    return archivo
def mostrar_datos(archivo:dict) -> bool:
    """Muestra los datos del json en consola
    Args:
        archivo (dict): JSON en forma de diccionario

    Returns:
        False: Hay algún error
        True: No hay errores

    """
    if len(archivo["usuarios"]) == 0:
        print("No hay usuarios listados")
        return False
    else:
        print("---Contenido actual del JSON---")
        for usuario in archivo["usuarios"]:
            print(f"ID: {usuario.get("id")} Nombre: {usuario.get("nombre")} Edad: {usuario.get("edad")} ")
        print("---Fin del contenido---")
        return True
def inicializar_datos(origen:str) -> bool:
    """Comprueba si hay algún error en el archivo origen
    Args:
        origen (str): archivo origen
    Returns:
        False: Hay algún error
        True: No hay errores
    """
    try:
        with open(origen, "r"):
            pass
    except FileNotFoundError:
        print("No se ha encontrado el archivo JSON. Asegúrate de que esté en el directorio raíz")
        return False
    except json.JSONDecodeError:
        print("Problemas al decodificar el JSON")
        return False
    else:
        print(f"Datos inicializados desde 'datos_usuarios_orig.json' a 'datos_usuarios.json'.")
        return True
def limpiar_consola():
        """ Limpia la consola"""
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
def espera():
    return input("Presione Enter para continuar")
def actualizar_edad(archivo:dict) -> None:
    """Actualiza la edad de un usuario
    Args:
        archivo (dict): archivo entrante
    Returns:
        None"""
    archivo["usuarios"][0]["edad"] = 26
    print("Actualizada la edad del usuario con id 1")
def insertar_usuario(archivo:dict) -> None:
    """Inserta un usuario
        Args:
            archivo (dict): archivo entrante
        Returns:
            None"""
    archivo["usuarios"].append(dict(id=3, nombre="Pedro", edad=40))
    print("Usuario Pedro añadido con éxito")
def eliminar_usuario(archivo:dict) -> None:
    """Elimina un usuario
            Args:
                archivo (dict): archivo entrante
            Returns:
                None"""
    del [archivo["usuarios"][1]]
    print("Usuario con ID 2 eliminado")
def actualizar_archivo(archivo:dict) -> None:
    """Crea un JSON nuevo con los datos actualizados
               Args:
                   archivo (dict): archivo entrante
               Returns:
                   None"""
    with open("datos_usuarios.json", "w") as f:
            json.dump(archivo,f, indent=4 )
    print("Operaciones completadas. Archivo actualizado.")
def main():
    if inicializar_datos("datos_usuarios_orig.json"):
        archivo = cargar_json("datos_usuarios_orig.json")
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