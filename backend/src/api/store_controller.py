from Models.store import Store, Categoria
from fastapi import HTTPException, Depends, Cookie, status, APIRouter, Query
from fastapi.responses import RedirectResponse, JSONResponse
import json

router = APIRouter()

# File to store user data
STORE_DATA_FILE = "store_data.json"


# Helper function to load user data from JSON file
def load_store_data():
    try:
        with open(STORE_DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


# Helper function to save user data to JSON file
def save_store_data(data):
    with open(STORE_DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# Endpoint for user sign-up
@router.post("/signup/")
async def signup(u: str, c: str, e: str, cat: Categoria, p: str):

    store = Store(username=u, cnpj=c, email=e, categoria=cat, password=p)

    store_data = load_store_data()

    if store.cnpj in store_data:
        raise HTTPException(status_code=400, detail="CPNJ already registered")

    store_data[store.cnpj] = {"password": store.password,
                              "username": store.username,
                              "email": store.email,
                              "categoria": store.categoria}

    save_store_data(store_data)

    return {"message": "Admin signed up successfully"}


# Endpoint for user login
@router.post("/login/")
async def login(cnpj: str, password: str):

    user_data = load_store_data()

    if cnpj not in user_data or user_data[cnpj]["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid CNPJ or password")

    username = user_data[cnpj]["username"]

    response = JSONResponse({"message": f'Logged in successfully, {username}'})

    response.set_cookie(key="cnpj", value=cnpj, httponly=True)

    return response


def change_password(new_password: str, cnpj: str):
    user_data = load_store_data()
    user = user_data[cnpj]
    user["password"] = new_password
    save_store_data(user)

def change_email(new_email: str, cnpj: str):
    user_data = load_store_data()
    user = user_data[cnpj]
    user["email"] = new_email
    save_store_data(user)

def change_username(new_username: str, cnpj: str):
    user_data = load_store_data()
    user = user_data[cnpj]
    user["username"] = new_username
    save_store_data(user)


# Endpoint for password retrieval
@router.post("/login/retrieve_password")
async def retrieve_password(cnpj: str, email: str, new_password: str):

    user_data = load_store_data()
    if cnpj in user_data:
        change_password(new_password, cnpj)
    else:
        raise HTTPException(status_code=400, detail="User not found")


# Dependency to check if user is logged in
def get_current_user(cnpj: str = Cookie(None)):
    user_data = load_store_data()
    if cnpj not in user_data:
        raise HTTPException(status_code=401, detail="You must be logged in")
    else:
        return {"message": "user data found"}


#Endpoint for account management
@router.post("/user/change_user_data")
def change_user_data(cnpj: str,
                            email: str | None,
                            password: str | None,
                            categoria: str | None,
                            username: str | None):

    user_data = load_store_data()
    if cnpj not in user_data:
        raise HTTPException(status_code=401, detail="User not found")

    if email:
        change_email(email, cnpj)
    if username:
        change_username(username, cnpj)
    if password:
        change_password(username, cnpj)



