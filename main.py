from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os



#open users json file

DATABASElol = 'user_database.json' 


#json helper functions

#read data from json file
def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} contains invalid JSON.")
        return None

#write data to json file
def write_json(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Successfully wrote data to {file_path}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")






app = FastAPI()






class User(BaseModel):
    name: str
    email: str
    password: str





# users = {
#     1: {
#         "name": "John Doe",
#         "email": "john@doe.com",
#         "password": "password"
#     }
# }

# @app.get("/get-users/{user_id}")
# def get_users(user_id: int):
#     return users[user_id]

# @app.post("/add-user/{user_id}")
# def add_user(user_id: int, user: User):
#     if user_id in users:
#         return {"Error" : "User ID already exists..."}
    
#     users[user_id] = {"name": user.name, "email": user.email, "password" : user.password}
#     return users[user_id]



@app.get("/get-data")
def fetch_my_data():
    data = read_json(DATABASElol)
    
    # Handle the case where the file doesn't exist
    if data is None:
        raise HTTPException(status_code=404, detail="JSON file not found.")
        
    # Handle the case where the file is corrupted or not valid JSON
    if data is False:
        raise HTTPException(status_code=500, detail="Error decoding the JSON file.")
        
    return data


@app.post("/register")
def register():
    return {"ToRegister" : "SomeName"}