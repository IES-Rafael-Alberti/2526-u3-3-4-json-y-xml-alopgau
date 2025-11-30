import json
import xml.etree.ElementTree as ET
import pytest
from convertidor import json_inicial, json_a_xml, xml_a_json


@pytest.mark.parametrize(
    "datos",
    [
        ({"usuarios": {"nombre": "Ana", "edad": 25}}),
        ({"usuarios": {"nombre": "Luis", "edad": 30, "activo": True}}),
    ]
)
def test_json_inicial(tmp_path, datos):
    ruta = tmp_path / "orig.json"
    with pytest.MonkeyPatch.context() as m:
        m.setenv("PYTHONIOENCODING", "utf-8")
        m.chdir(tmp_path)
        json_inicial(datos)
        with open("datos_convertidor_orig.json", "r") as f:
            cargado = json.load(f)
    assert cargado == datos


@pytest.mark.parametrize(
    "entrada,esperado_tags",
    [
        ({"usuarios": {"nombre": "Ana", "edad": 25}}, ["nombre", "edad"]),
        ({"usuarios": {"a": 1, "b": 2, "c": 3}}, ["a", "b", "c"]),
    ]
)
def test_json_a_xml(tmp_path, entrada, esperado_tags):
    ruta_json = tmp_path / "datos_convertidor_orig.json"
    with open(ruta_json, "w") as f:
        json.dump(entrada, f)

    with pytest.MonkeyPatch.context() as m:
        m.chdir(tmp_path)
        json_a_xml("datos_convertidor_orig.json")
        arbol = ET.parse("datos_convertidor.xml")
        raiz = arbol.getroot()

    assert raiz.tag == "usuarios"
    assert [elem.tag for elem in raiz] == esperado_tags


@pytest.mark.parametrize(
    "xml_contenido,esperado_json",
    [
        ("<usuarios><nombre>Ana</nombre><edad>25</edad></usuarios>",
         {"usuarios": None, "nombre": "Ana", "edad": "25"}),

        ("<usuarios><a>1</a><b>2</b></usuarios>",
         {"usuarios": None, "a": "1", "b": "2"}),
    ]
)
def test_xml_a_json(tmp_path, xml_contenido, esperado_json):
    ruta_xml = tmp_path / "datos_convertidor.xml"
    ruta_json = tmp_path / "datos_convertidor.json"

    ruta_xml.write_text(xml_contenido, encoding="utf-8")

    with pytest.MonkeyPatch.context() as m:
        m.chdir(tmp_path)
        xml_a_json("datos_convertidor.xml")
        with open("datos_convertidor.json", "r") as f:
            cargado = json.load(f)

    assert cargado == esperado_json
