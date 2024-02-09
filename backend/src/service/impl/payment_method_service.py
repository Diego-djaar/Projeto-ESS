from src.db.__init__ import database as db
from src.schemas.payment_schema import Boleto_pix


class payment_service:

    @staticmethod
    def inserting_method(boleto: Boleto_pix):
        result = db.add("payments", boleto)
        return result 
