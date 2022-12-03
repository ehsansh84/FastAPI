from fastapi import FastAPI
import os
import uvicorn
from enum import Enum

app = FastAPI()


class UserRole(str, Enum):
    admin = "admin"
    user = "user"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@app.get("/users/{user_role}")
async def read_user(user_role):
    if user_role == UserRole.user:
        return {"role": "A user role!"}
    else:
        return {"role": "An admin role"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8100)
