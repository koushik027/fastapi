from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app=FastAPI()
class Name(BaseModel):
     stud_name:str 
     stud_id:str
     stud_branch:str
     stud_section:str
@app.get("/")
def basic():
     return"welcome to student registeration"
     
@app.get("/student")
def det(name_var:Name):
    return a

a=[]

@app.post("/studentrecord")
def name(name_var:Name):
    item=dict()
    name_encoded=jsonable_encoder(name_var)
    fname=name_encoded['stud_name']
    srn=name_encoded['stud_id']
    branch=name_encoded['stud_branch']
    section=name_encoded['stud_section']
    item.update({"stud_name":fname,"stud_id":srn,"stud_branch":branch,"stud_section":section})
    a.append(item)
    return "registered"

@app.put("/studentrecord/{stud_id}")
async def update_item(stud_id: str,name_var:Name):
    update_item_encoded=jsonable_encoder(name_var)
    for p in a:
        if p['stud_id']==stud_id:
           p['stud_section']= 'C'
    return a
@app.delete("studentrecord/{stud_id}")
def del_item(stud_id:str ,name_var:Name):
    for p in a:
        if p['stud_id']==stud_id:
           del p
    return a