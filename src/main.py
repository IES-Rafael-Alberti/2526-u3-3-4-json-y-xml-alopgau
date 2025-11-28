import json
import os
def mostrar_datos(archivo:dict) -> None:
    """Muestra los datos del json en consola
    Args:
        archivo (dict): JSON en forma de diccionario

    Returns:
        None

    """
    if len(archivo["usuarios"]) == 0:
        print("No hay usuarios listados")
    print("---Contenido actual del JSON---")
    for usuario in archivo["usuarios"]:
        print(f"ID: {usuario.get("id")} Nombre: {usuario.get("nombre")} Edad: {usuario.get("edad")} ")
    print("---Fin del contenido---")
def inicializar_datos() -> bool | dict:
    """Copia el contenido del archivo a un archivo datos_usuarios.json
    """
    try:
        with open("datos_usuarios_orig.json", "r") as f:
            archivo = json.load(f)
    except FileNotFoundError:
        print("No se ha encontrado el archivo JSON. Asegúrate de que esté en el directorio raíz")
        return False
    except json.JSONDecodeError:
        print("Problemas al decodificar el JSON")
        return False
    else:
        print(f"Datos inicializados desde 'datos_usuarios_orig.json' a 'datos_usuarios.json'.")
        return archivo
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
    """Actualiza el JSON
               Args:
                   archivo (dict): archivo entrante
               Returns:
                   None"""
    with open("datos_usuarios_procesados.json", "w") as f:
            json.dump(archivo,f, indent=4 )
    print("Operaciones completadas. Archivo actualizado.")
def main():
    if inicializar_datos():
        archivo = inicializar_datos()
        mostrar_datos(archivo)
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