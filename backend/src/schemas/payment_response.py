from typing import Optional
from pydantic import BaseModel
from .response import HttpResponseModel

class HTTPPaymentResponse:

    @staticmethod
    def INSERTION_SUCESSFULLY() -> HttpResponseModel: 
        return HttpResponseModel (
            message="Payment method has been inserted sucessfully",
            status_code=201
        )