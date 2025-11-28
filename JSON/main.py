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
    Args:
    Returns:
        archivo_nuevo (dict) archivo json nuevo
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
def actualizar_edad(archivo:dict)
def main():
        if inicializar_datos():
            archivo = inicializar_datos()
            mostrar_datos(archivo)
            espera()
            limpiar_consola()
            actualizar_edad(archivo)
            espera()
            limpiar_consola()
            insertar_usuario(archivo)
            espera()
            limpiar_consola()
            eliminar_usuario(archivo)


if __name__ == "__main__":
    main()