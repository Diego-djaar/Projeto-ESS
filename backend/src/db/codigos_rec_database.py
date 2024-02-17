import datetime
import jsonpickle

class Recuperacao(object):
    email:str
    codigo:str
    date: datetime.date

    def __init__(self, email: str, codigo: str, date: datetime.date = datetime.datetime.now()) -> None:
        self.email = email
        self.codigo = codigo
        self.date = date


class RecuperacaoDatabase():
    db: dict[Recuperacao]
    file_path: str

    def __init__(self, path = "Códigos.json"):
        self.db = dict()
        self.file_path = path
        self.try_read_from_file()

    def try_read_from_file(self):
        # Ler users de um arquivo
        import os.path
        if not os.path.exists(self.file_path):
            self.write_to_file()
            return None
        
        with open(self.file_path) as f:
            objetos = f.read()
            db = jsonpickle.decode(objetos)
            if type(db) == dict:
                self.db = db

    def write_to_file(self):
        objetos = jsonpickle.encode(self.db)
        with open(self.file_path, 'w+') as f:
            f.write(objetos)

    def add_recuperacao(self, recuperacao: Recuperacao):
        self.db[recuperacao.email] = recuperacao
        self.write_to_file()
        return True