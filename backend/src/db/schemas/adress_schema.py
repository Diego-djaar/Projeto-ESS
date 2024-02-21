class Endereço():
    rua: str
    numero: int
    bairro: str
    cidade: str
    estado: str
    cep: str
    pais: str
    complemento: str | None

    def __init__(self, rua: str, numero: int, bairro: str, cidade: str, estado: str, cep: str, pais: str, complemento: str | None = None):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.pais = pais
        self.complemento = complemento

    def __str__(self):
        endereco_completo = f"{self.rua}, {self.numero}"
        if self.complemento:
            endereco_completo += f", {self.complemento}"
        endereco_completo += f"\n{self.bairro}, {self.cidade} - {self.estado}\nCEP: {self.cep}\n{self.pais}"
        return endereco_completo
