from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco

#criando classe abstrata
class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, salario: float, endereco: Endereco) -> None:
        super().__init__()
        self.nome = self._verificar_nome(nome)
        self.telefone = telefone
        self.email = email
        self.salario = self._verificar_salario(salario)
        self.endereco = endereco

#criando metodo salario
    @abstractmethod
    def salario_final(float, salario):
        return salario

#criando metodo de exceção
    def _verificar_nome(self, nome:str) -> str:
        if not isinstance(nome, str):
            raise TypeError("Digite apenas texto para os nome.")
        if not nome.strip():
            raise ValueError("Nome precisa conter informação.")
        return nome
    
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