from fastapi import FastAPI, HTTPException
from typing import Dict

app = FastAPI()


students_db: Dict[int, dict] = {}


class Student:
    def __init__(self, name: str, age: int, sex: str, height: float):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height


@app.post("/students/")
def create_student(name: str, age: int, sex: str, height: float):
    student_id = len(students_db) + 1
    student_data = {
        "name": name,
        "age": age,
        "sex": sex,
        "height": height
    }
    students_db[student_id] = student_data
    return student_data


@app.get("/students/{student_id}")
def read_student(student_id: int):
    student = students_db.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.get("/students/")
def read_students():
    return students_db


@app.put("/students/{student_id}")
def update_student(student_id: int, name: str, age: int, sex: str, height: float):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    student_data = {
        "name": name,
        "age": age,
        "sex": sex,
        "height": height
    }
    students_db[student_id] = student_data
    return student_data


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    del students_db[student_id]
    return {"message": "Student deleted successfully"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)