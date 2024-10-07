import pytest

from projeto.models.endereco import Endereco
from projeto.models.medico import Medico
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def teste_medico():
    medico1 = Medico("José", "11 9 7777-7777", "Jose@gmail.com", 7000.0, "321", Endereco("Avenida X", "854", "Rua X", "44666-406", "São Paulo", UnidadeFederativa.SAO_PAULO))
    return medico1

def test_validar_nome_vazio(teste_medico):
    with pytest.raises(ValueError, match="Nome não pode conter espaços vazios."):
     Medico("", "11 9 7777-7777", "Jose@gmail.com", 7000.0, "321", Endereco("Avenida X", "854", "Rua X", "44666-406", "São Paulo", UnidadeFederativa.SAO_PAULO))

def test_validar_nome_tipo_str(teste_medico):
    with pytest.raises(TypeError, match="Digite apenas texto para os nome."):
     Medico(123, "11 9 7777-7777", "Jose@gmail.com", 7000.0, "321", Endereco("Avenida X", "854", "Rua X", "44666-406", "São Paulo", UnidadeFederativa.SAO_PAULO))

def test_validar_telefone_vazio(teste_medico):
    with pytest.raises(ValueError, match="Telefone não pode conter espaços vazios."):
     Medico("José", "", "Jose@gmail.com", 7000.0, "321", Endereco("Avenida X", "854", "Rua X", "44666-406", "São Paulo", UnidadeFederativa.SAO_PAULO))

def test_validar_email_vazio(teste_medico):
    with pytest.raises(ValueError, match="Email não pode conter espaços vazios."):
     Medico("José", "11 9 7777-7777", "", 7000.0, "321", Endereco("Avenida X", "854", "Rua X", "44666-406", "São Paulo", UnidadeFederativa.SAO_PAULO))

def test_validar_salario_tipo_float(teste_medico):
    with pytest.raises(TypeError, match="Digite apenas numeros para salario."):
     Medico("José", "11 9 7777-7777", "Jose@gmail.com", "Cinco Mil", "321", Endereco("Avenida X", "854", "Rua X", "44666-406", "São Paulo", UnidadeFederativa.SAO_PAULO))

def test_validar_salario_positivo(teste_medico):
    with pytest.raises(ValueError, match="Digite apenas numeros positivos para salario."):
     Medico("José", "11 9 7777-7777", "Jose@gmail.com", -7000.0, "321", Endereco("Avenida X", "854", "Rua X", "44666-406", "São Paulo", UnidadeFederativa.SAO_PAULO))

def test_validar_nome_engenheiro(teste_medico):
    assert teste_medico.nome == "José"

def test_validar_nome_engenheiro(teste_medico):
    assert teste_medico.telefone == "11 9 7777-7777"

def test_validar_nome_engenheiro(teste_medico):
    assert teste_medico.email == "Mrt@gmail.com"

def test_validar_nome_engenheiro(teste_medico):
    assert teste_medico.salario == 7000.0

def test_validar_nome_engenheiro(teste_medico):
    assert teste_medico.crea == "321"

def test_validar_nome_engenheiro(teste_medico):
    assert teste_medico.logradouro == "Avenida X"

def test_validar_nome_engenheiro(teste_medico):
    assert teste_medico.numero == "854"

def test_validar_nome_engenheiro(teste_medico):
    assert teste_medico.complemento == "Rua X"

def test_validar_nome_engenheiro(teste_medico):
    assert teste_medico.cep == "44666-406"

def test_validar_nome_engenheiro(teste_medico):
    assert teste_medico.cidade == "São Paulo"

def test_validar_nome_engenheiro(teste_medico):
    assert teste_medico.endereco.uf == UnidadeFederativa.SAO_PAULO