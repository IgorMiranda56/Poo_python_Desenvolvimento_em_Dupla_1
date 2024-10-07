from projeto.models.endereco import Endereco
from projeto.models.funcionario import Funcionario

#Definindo classe
class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, salario: float, crm: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, salario, endereco)
        self.crm = crm

#Definindo exceção para atributo
    def _verificar_nome(self, nome: str) -> str:
        return super()._verificar_nome(nome)
    
    def _verificar_salario(self, salario: float) -> float:
        return super()._verificar_salario(salario)
    
    def _verificar_email(self, email: str) -> str:
        return super()._verificar_email(email)
    
    def _verificar_telefone(self, telefone: str) -> str:
        return super()._verificar_telefone(telefone)
    
    #def salario_final(float, salario):
        #return super().salario_final(salario)
    
#Tostring()
    def __str__(self) -> str:
        return (super().__str__() +
                f"\nCrm: {self.crm}")
