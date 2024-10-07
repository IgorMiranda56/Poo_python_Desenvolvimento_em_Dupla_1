from projeto.models.enums.unidade_federativa import UnidadeFederativa

class Endereco():
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, uf: UnidadeFederativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf 

        def __str__(self) -> str:
            return (f"Logradouro: {self.logradouro}"
                    f"Número: {self.numero}"
                    f"Complemento: {self.complemento}"
                    f"CEP: {self.cep}"
                    f"Cidade: {self.cidade}"
                    f"UF: {self.texto} / {self.sigla}")