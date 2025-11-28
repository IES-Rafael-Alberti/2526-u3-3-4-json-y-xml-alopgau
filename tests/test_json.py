import pytest
from main import actualizar_edad, insertar_usuario, eliminar_usuario

@pytest.mark.parametrize(
    "archivo_inicial, esperado_edad",
    [
        (
            {"usuarios": [{"id":1, "nombre":"Ana", "edad":25}]},
            26
        ),
        (
            {"usuarios": [{"id":1, "nombre":"Luis", "edad":30}]},
            26
        ),
    ]
)
def test_actualizar_edad(archivo_inicial, esperado_edad):
    actualizar_edad(archivo_inicial)
    assert archivo_inicial["usuarios"][0]["edad"] == esperado_edad


@pytest.mark.parametrize(
    "archivo_inicial, esperado_ids",
    [
        (
            {"usuarios":[{"id":1,"nombre":"Ana","edad":26}]},
            [1, 3]
        ),
        (
            {"usuarios":[{"id":1,"nombre":"Luis","edad":26},{"id":2,"nombre":"Marta","edad":30}]},
            [1, 2, 3]
        ),
    ]
)
def test_insertar_usuario(archivo_inicial, esperado_ids):
    insertar_usuario(archivo_inicial)
    ids_resultantes = [u["id"] for u in archivo_inicial["usuarios"]]
    assert ids_resultantes == esperado_ids


@pytest.mark.parametrize(
    "archivo_inicial, esperado_ids",
    [
        (
            {"usuarios":[{"id":1,"nombre":"Ana","edad":26},{"id":2,"nombre":"Luis","edad":30}]},
            [1]
        ),
        (
            {"usuarios":[{"id":1,"nombre":"Luis","edad":26},{"id":2,"nombre":"Marta","edad":30},{"id":3,"nombre":"Pedro","edad":40}]},
            [1,3]
        ),
    ]
)
def test_eliminar_usuario(archivo_inicial, esperado_ids):
    eliminar_usuario(archivo_inicial)
    ids_resultantes = [u["id"] for u in archivo_inicial["usuarios"]]
    assert ids_resultantes == esperado_ids
