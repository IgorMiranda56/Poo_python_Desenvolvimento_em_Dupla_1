from abc import ABC
from projeto.models.endereco import Endereco

#criando classe abstrata
class Funcionareio(ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        super().__init__()
        self.nome = self._verificar_nome(nome)
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

#criando metodo salario
    
#criando metodo de exceção
    def _verificar_nome(self, nome:str) -> str:
        if not isinstance(nome, str):
            raise TypeError("Digite apenas texto para os nome.")
        if not nome.strip():
            raise ValueError("Nome precisa conter informação.")
        return nome



#criando tostring()
    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\nEndereço: {self.endereco}")