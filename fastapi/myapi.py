from fastapi import FastAPI , Path 
from typing import Optional
from pydantic import BaseModel 
app = FastAPI()

students = { 
    1:{
    "name" : 'aavash' , 
    "age" : 22 , 
    "year" : "BCT"
    }
}
class Student(BaseModel):
    name: str 
    age : int 
    year : str

class UpdateStudent(BaseModel): 
    name: Optional[str] = None
    age: Optional[int] = None 
    year : Optional[str] = None
@app.get("/")
def index():
    return{"name" : "First Data "}



@app.get("/get-student/{student_id}")
def get_student(student_id : int = Path(..., description= "The ID of the student you want to view" , gt =0,lt = 26)): 
    return students[student_id]


@app.get("/get-by-name/{student_id}")
def get_student(* ,student_id : int ,test :int, name: Optional[str]= None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"data" : " not  found"}


@app.post("/create-student/{student_id}")
def create_student(student_id : int , student : Student):
    if student_id in students: 
        return{"Error" : "Student doesnt exist"}

    students[student_id] = student 
    return students[student_id]

@app.put("/update-student/{studnet_id}")
def update_student(student_id: int , student: UpdateStudent):
    if student_id in students:
        return {"error" : "sorry"} 
    
    if student.name != None: 
        students[student_id].name = student.name 

    if student.age != None: 
        students[student_id].age = student.age 

    if student.year != None: 
        students[student_id].year = student.year

    return students[student_id]