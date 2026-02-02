from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db import get_connection


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
    user_id:int
    name:str
    age:int
    gender:str
   
    email:str
   

class Update(BaseModel):
    updating:str
    updater:str



# get user information via id 
@information.get("/members")
def members_info(user_id:int):
    #calling the db
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM patients WHERE user_id = %s",
        (user_id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    user_do_not_exists(user_id)
    return row





# create patient profile
@information.post("/members")
def add_profile(new_info:User):
    #calling the db
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT user_id FROM patients WHERE user_id = %s",(new_info.user_id,))
    checker=cursor.fetchone()
    if  checker:
         cursor.close()
         conn.close()
         raise HTTPException(
             status_code=400,
             detail="Patient ID already exists")
    
    else:
        cursor.execute(
            "insert into patients (user_id,name,age,gender,email) values(%s,%s,%s,%s,%s)",
            (new_info.user_id,
             new_info.name,
             new_info.age,
             new_info.gender,
             new_info.email
         )

    )

   
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Patient info added"}




#updating patient info 

@information.put("/members/{user_id}")
def update_info(user_id:int,new_info:User):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""update patients set name=%s, 
                     age =%s ,
                     gender=%s,
                     email=%s 
                    where user_id=%s;""",
                    (new_info.name,new_info.age,new_info.gender,new_info.email,new_info.user_id))
    cursor.execute("select * from patients where user_id=%s",(new_info.user_id,))
    row=cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()

    return row
    # user_do_not_exists(user_id)
    # user[user_id]={"user_id":new_info.user_id, 
    #                 "name":new_info.name,
    #                 "age":new_info.age,
    #                 "gender":new_info.gender,
    #                 "phone":new_info.phone,
    #                 "email":new_info.email,
    #                 "emergency_contact":new_info.emergency_contact}
    # return user[user_id]

# @information.put("/members/specific/{user_id}")
# def update_pro(user_id:int,new_info:Update):
#     user_do_not_exists(user_id)
#     if new_info.updating not in user[user_id]:
#         raise HTTPException(status_code=400, detail="Invalid field name")
#     else:
#         user[user_id][new_info.updating]=new_info.updater
        
#     return {"message": "Field updated", "data": user[user_id]}
