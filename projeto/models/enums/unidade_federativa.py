from enum import Enum

#Determinando atributos
class UnidadeFederativa(Enum):
    BAHIA = ("Bahia", "BA")
    SAO_PAULO = ("São Paulo","SP")
    RIO_DE_JANEIRO = ("Rio de Janeiro","RJ")

    def __init__(self, texto: str, sigla: str) -> None:
        self.texto = texto
        self.sigla = sigla