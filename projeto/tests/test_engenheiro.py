import pytest

from projeto.models.endereco import Endereco
from projeto.models.engenheiro import Engenheiro
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def teste_engenheiro():
    engenheiro1 = Engenheiro("Marta", "71 9 9999-9999", "Mtr@gmail.com", 5000.0, "789", Endereco("Avenida A", "715", "Rua A", "40400-400", "Salvador", UnidadeFederativa.BAHIA))
    return engenheiro1

def test_validar_nome_vazio(teste_engenheiro):
    with pytest.raises(ValueError, match="Nome não pode conter espaços vazios."):
        Engenheiro("", "71 9 9999-9999", "Mtr@gmail.com", 5000.0, "789", Endereco("Avenida A", "715", "Rua A", "40400-400", "Salvador", UnidadeFederativa.BAHIA))

def test_validar_nome_tipo_str(teste_engenheiro):
    with pytest.raises(TypeError, match="Digite apenas texto para os nome."):
        Engenheiro(123, "71 9 9999-9999", "Mtr@gmail.com", 5000.0, "789", Endereco("Avenida A", "715", "Rua A", "40400-400", "Salvador", UnidadeFederativa.BAHIA))

def test_validar_telefone_vazio(teste_engenheiro):
    with pytest.raises(ValueError, match="Telefone não pode conter espaços vazios."):
        Engenheiro("Marta", "", "Mtr@gmail.com", 5000.0, "789", Endereco("Avenida A", "715", "Rua A", "40400-400", "Salvador", UnidadeFederativa.BAHIA))

def test_validar_email_vazio(teste_engenheiro):
    with pytest.raises(ValueError, match="Email não pode conter espaços vazios."):
        Engenheiro("Marta", "71 9 9999-9999", "", 5000.0, "789", Endereco("Avenida A", "715", "Rua A", "40400-400", "Salvador", UnidadeFederativa.BAHIA))

def test_validar_salario_tipo_float(teste_engenheiro):
    with pytest.raises(TypeError, match="Digite apenas numeros para salario."):
        Engenheiro("Marta", "71 9 9999-9999", "Mtr@gmail.com", "Cinco Mil", "789", Endereco("Avenida A", "715", "Rua A", "40400-400", "Salvador", UnidadeFederativa.BAHIA))

def test_validar_salario_positivo(teste_engenheiro):
    with pytest.raises(ValueError, match="Digite apenas numeros positivos para salario."):
        Engenheiro("Marta", "71 9 9999-9999", "Mtr@gmail.com", -5000.0, "789", Endereco("Avenida A", "715", "Rua A", "40400-400", "Salvador", UnidadeFederativa.BAHIA))

def test_validar_nome_engenheiro(teste_engenheiro):
    assert teste_engenheiro.nome == "Marta"

def test_validar_nome_engenheiro(teste_engenheiro):
    assert teste_engenheiro.telefone == "71 9 9999-9999"

def test_validar_nome_engenheiro(teste_engenheiro):
    assert teste_engenheiro.email == "Mrt@gmail.com"

def test_validar_nome_engenheiro(teste_engenheiro):
    assert teste_engenheiro.salario == 5000.0

def test_validar_nome_engenheiro(teste_engenheiro):
    assert teste_engenheiro.crea == "789"

def test_validar_nome_engenheiro(teste_engenheiro):
    assert teste_engenheiro.logradouro == "Avenida A"

def test_validar_nome_engenheiro(teste_engenheiro):
    assert teste_engenheiro.numero == "715"

def test_validar_nome_engenheiro(teste_engenheiro):
    assert teste_engenheiro.complemento == "Rua A"

def test_validar_nome_engenheiro(teste_engenheiro):
    assert teste_engenheiro.cep == "40400-400"

def test_validar_nome_engenheiro(teste_engenheiro):
    assert teste_engenheiro.cidade == "Salvador"

def test_validar_nome_engenheiro(teste_engenheiro):
    assert teste_engenheiro.endereco.uf == UnidadeFederativa.BAHIA