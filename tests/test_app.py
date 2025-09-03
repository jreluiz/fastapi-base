from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_base.app import app


def test_root_dev_retornar_ola_mundo():
    # teste com 3 etapas (AAA)
    # A = Arrange - Arranjo
    # A = Act     - Executa a coisa
    # A = Assert  - Garanta que A é A

    # Arrange
    client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'Olá mundo!'}
    assert response.status_code == HTTPStatus.OK
