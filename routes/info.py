from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

information = APIRouter()





#data set
user = {
    1: {
        "user_id": "1",
        "name": "Aarav Mehta",
        "age": "34",
        "gender": "male",
        "phone": "9876543210",
        "email": "aarav.mehta@example.com",
        "emergency_contact": "Riya Mehta"
    },
    2: {
        "user_id": "2",
        "name": "Sara Khan",
        "age": "28",
        "gender": "female",
        "phone": "9123456780",
        "email": "sara.khan@example.com",
        "emergency_contact": "Imran Khan"
    }
}


#helper functions
def user_exists(a):
    if a  in user:
         raise HTTPException(status_code=400, detail="Patient ID already exists, profile denied") 

def user_do_not_exists(a):
    if a not in user:
         raise HTTPException(status_code=400, detail="Patient ID does not  exists") 


    
# Base models
class User(BaseModel):
    user_id:str
    name:str
    age:str
    gender:str
    phone:str
    email:str
    emergency_contact:str

class Update(BaseModel):
    updating:str
    updater:str



# get user information via id 
@information.get("/members")
def members_info(user_id:int):
    user_do_not_exists(user_id)
    return user[user_id]





# create patient profile
@information.post("/members")
def add_profile(new_info:User):
    if new_info.user_id  in user:
       raise HTTPException(status_code=400, detail="Patient ID already exists, profile denied")

    else:
        user[new_info.user_id]={"user_id":new_info.user_id, 
                                "name":new_info.name,
                                "age":new_info.age,
                                "gender":new_info.gender,
                                "phone":new_info.phone,
                                "email":new_info.email,
                                "emergency_contact":new_info.emergency_contact}
        return "patient info added"


# updating personal info 



#updating patient info 

@information.put("/members/{user_id}")
def update_info(user_id:int,new_info:User):
    user_do_not_exists(user_id)
    user[user_id]={"user_id":new_info.user_id, 
                    "name":new_info.name,
                    "age":new_info.age,
                    "gender":new_info.gender,
                    "phone":new_info.phone,
                    "email":new_info.email,
                    "emergency_contact":new_info.emergency_contact}
    return user[user_id]

@information.put("/members/specific/{user_id}")
def update_pro(user_id:int,new_info:Update):
    user_do_not_exists(user_id)
    if new_info.updating not in user[user_id]:
        raise HTTPException(status_code=400, detail="Invalid field name")
    else:
        user[user_id][new_info.updating]=new_info.updater
        
    return {"message": "Field updated", "data": user[user_id]}
