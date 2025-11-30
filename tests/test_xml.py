import pytest
import xml.etree.ElementTree as ET
from main_xml import actualizar_edad, insertar_usuario, eliminar_usuario


def crear_xml_en_memoria(usuarios):
    raiz = ET.Element("usuarios")
    for u in usuarios:
        usuario = ET.SubElement(raiz, "usuario")
        ET.SubElement(usuario, "id").text = str(u["id"])
        ET.SubElement(usuario, "nombre").text = u["nombre"]
        ET.SubElement(usuario, "edad").text = str(u["edad"])
    return ET.ElementTree(raiz)


@pytest.mark.parametrize(
    "usuarios_inicial, edad_esperada",
    [
        ([{"id":1, "nombre":"Ana", "edad":25}], "31"),
        ([{"id":1, "nombre":"Luis", "edad":50}], "31"),
    ]
)
def test_actualizar_edad(usuarios_inicial, edad_esperada):
    arbol = crear_xml_en_memoria(usuarios_inicial)
    actualizar_edad(arbol)
    assert arbol.find("usuario").find("edad").text == edad_esperada


@pytest.mark.parametrize(
    "usuarios_inicial, ids_esperados",
    [
        ([{"id":1,"nombre":"Ana","edad":31}], ["1", "3"]),
        ([{"id":1,"nombre":"Luis","edad":31}, {"id":2,"nombre":"Marta","edad":33}], ["1", "2", "3"]),
    ]
)
def test_insertar_usuario(usuarios_inicial, ids_esperados):
    arbol = crear_xml_en_memoria(usuarios_inicial)
    insertar_usuario(arbol)

    ids_resultantes = [u.find("id").text for u in arbol.getroot().findall("usuario")]
    assert ids_resultantes == ids_esperados


@pytest.mark.parametrize(
    "usuarios_inicial, ids_esperados",
    [
        ([{"id":1,"nombre":"Ana","edad":31}, {"id":2,"nombre":"Luis","edad":30}], ["1"]),
        ([{"id":1,"nombre":"Luis","edad":31}, {"id":2,"nombre":"Marta","edad":33}, {"id":3,"nombre":"Pedro","edad":40}], ["1", "3"]),
    ]
)
def test_eliminar_usuario(usuarios_inicial, ids_esperados):
    arbol = crear_xml_en_memoria(usuarios_inicial)
    eliminar_usuario(arbol)

    ids_resultantes = [u.find("id").text for u in arbol.getroot().findall("usuario")]
    assert ids_resultantes == ids_esperados
