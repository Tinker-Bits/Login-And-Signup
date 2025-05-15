import firebase_admin
from firebase_admin import credentials,firestore
import os
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
path = os.environ.get("Firebase")
cred = credentials.Certificate(path)
firebase_admin.initialize_app(cred)
db = firestore.client()
collection = db.collection('Users')
def get_new_id():
    return (collection.count()).get()[0][0].value+1
system = FastAPI()
class user(BaseModel):
    first_name: str
    password: str
    username: str
    confirm_password: str
    middle_name:str
    last_name:str
    age: int
    professional_title: str
@system.post('/signup')
def signup(user_instance: user):
    username_query = collection.where("username", "==", user_instance.username).limit(1).get()
    if username_query:
        raise HTTPException(status_code=400, detail="Username already exists")
    if(user_instance.password==user_instance.confirm_password):
        collection.document(f'{get_new_id()}').set(
            {
                "first_name": user_instance.first_name,
                "username": user_instance.username,
                "password": user_instance.password,
                "middle_name": user_instance.middle_name,
                "last_name": user_instance.last_name,
                "age": user_instance.age,
                "professional_title": user_instance.professional_title
            }
        )
    else:
        raise HTTPException(status_code=400,detail="Password And Confrim Password Feild Not Same")
@system.post('/signin')
def signin():
    return()
