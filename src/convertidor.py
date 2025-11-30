import json
import xml.etree.ElementTree as ET
from textwrap import indent


def json_inicial(datos:dict) -> None:
    """Convierte los datos iniciales a JSON
    Args:
        datos (dict): Datos de origen
    """
    with open("datos_convertidor_orig.json", "w") as archivo:
        json.dump(datos,archivo, indent=4)
def json_a_xml(ruta:str) -> None:
        """ Convierte de json a xml
            Args:
                ruta (str): Archivo json inicial
            Returns:
                None
            """
        with open(ruta, "r") as archivo:
            archivo_cargado = json.load(archivo)
            raiz = ET.Element("usuarios")
            arbol = ET.ElementTree(raiz)
            for clave,valor in zip(archivo_cargado["usuarios"].keys(), archivo_cargado["usuarios"].values()):
                ET.SubElement(raiz,clave).text = str(valor)
            arbol.write("datos_convertidor.xml", encoding="utf-8", xml_declaration=True)
def xml_a_json(ruta:str) -> None:
        """ Convierte de xml a json
                    Args:
                        ruta (str): Archivo xml inicial
                    Returns:
                        None
                    """
        arbol = ET.parse(ruta)
        raiz = arbol.getroot()
        json_archivo = dict()
        for elem in raiz.iter():
            json_archivo.setdefault(elem.tag,elem.text)
        with open("datos_convertidor.json", "w") as destino:
            json.dump(json_archivo,destino, indent=4)



def main():
    datos = { "usuarios": {
    "nombre": "Ana",
    "edad": 25,
    "habilidades": ["HTML", "CSS"],
    "activo": False
}
}
    json_inicial(datos)
    json_a_xml("datos_convertidor_orig.json")
    xml_a_json("datos_convertidor.xml")

if __name__ == "__main__":
    main()