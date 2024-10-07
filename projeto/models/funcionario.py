from abc import ABC
from projeto.models.endereco import Endereco

#criando classe abstrata
class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, salario: float, endereco: Endereco) -> None:
        super().__init__()
        self.nome = self._verificar_nome(nome)
        self.telefone = self._verificar_telefone(telefone)
        self.email = self._verificar_email(email)
        self.salario = self._verificar_salario(salario)
        self.endereco = endereco

#criando metodo de exceção
    def _verificar_nome(self, nome:str) -> str:
        if not isinstance(nome, str):
            raise TypeError("Digite apenas texto para os nome.")
        if not nome.strip():
            raise ValueError("Nome não pode conter espaços vazios.")
        return nome
    
    def _verificar_telefone(self, telefone: str) -> str:
        if not telefone.strip():
            raise ValueError("Telefone não pode conter espaços vazios.")
        return telefone
    
    def _verificar_email(self, email: str) -> str:
        if not email.strip():
            raise ValueError("Email não pode conter espaços vazios.")
        return email
    
    def _verificar_salario(self, salario:float) -> float:
        if not isinstance(salario, float):
            raise TypeError("Digite apenas numeros para salario.")
        if salario < 0:
            raise ValueError("Digite apenas numeros positivos para salario.")
        return salario 

#criando tostring()
    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\nEndereço: {self.endereco}")