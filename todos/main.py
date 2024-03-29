from fastapi import FastAPI
import uvicorn

app = FastAPI()


students = [{
    "studentId":1,
    "name": "John Doe",
    "age": 25,
    "grade":10

}]

# Get All The Students From The APPi

@app.get("/getStudents")
def get_Students():
    print("all students are here")
    return students


# Get One Specific Student With Its ID

@app.get("/getOneStudent/{item_id}")
def get_OneStudent(item_id:int):
    if item_id < len(students):
        return students[item_id]
    else:
        return  {"msg":f"Item with id {item_id} not found"}
    
# Add A Student With It's Credentials

@app.post( "/addStudent")
def add_Student(studentId:int, name:str, age:int,grade:int):
    student={
        "studentId":studentId,
        "name": name,
        "age": age,
        "grade":grade
    }
    students.append(student)
    return {"msg":f"New Student added successfully","data":student}

# Update A Student With It's ID



@app.put("/updateStudent/{student_id}")
def update_student(student_id:int, name:str, age:int,grade:int):
    for i in range(len(students)):
        if  students[i]['studentId'] == student_id :
            students[i].update({'name': name,'age':age,'grade':grade})
            return {"msg":f"Student updated successfully","data":students[i]}
    return {"msg":f"No student with the id {student_id} was found."}


# Delete A Student With It's ID


@app.delete("/removeStudent/{student_id}")
def remove_student(student_id: int):
    for i, student in enumerate(students):
        if student['studentId'] == student_id:
            students.pop(i)
            return {"msg": "Student removed successfully"}
    return {"msg": f"No student with the id {student_id} was found."}

  

def start():
    uvicorn.run("todos.main:app", host="127.0.0.1", port=8000, reload=True )