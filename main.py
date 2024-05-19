from fastapi import FastAPI
from schemas import Student
import mysql.connector

app = FastAPI()

db_config = {
    "host": "100.27.52.36",
    "port": 8005,
    "user": "root",
    "password": "utec",
    "database": "api_estudiantes"
}

@app.post("/estudiantes")
def add_student(student: Student):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = "INSERT INTO estudiantes (nombre, apellido, fecha_de_nacimiento) VALUES (%s, %s, %s)"
    val = (student.nombre, student.apellido, student.fecha_de_nacimiento)
    cursor.execute(sql, val)
    conn.commit()
    conn.close()
    return {"message": "Student added successfully"}

@app.get("/estudiantes")
def get_students():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudiantes")
    students = cursor.fetchall()
    conn.close()
    return {"students": students}

@app.get("/estudiantes/{id}")
def get_student(id: int):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudiantes WHERE id = %s", (id,))
    student = cursor.fetchone()
    conn.close()
    return {"student": student}

@app.put("/estudiantes/{id}")
def update_student(id: int, student: Student):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = "UPDATE estudiantes SET nombre=%s, apellido=%s, fecha_de_nacimiento=%s WHERE id=%s"
    val = (student.nombre, student.apellido, student.fecha_de_nacimiento, id)
    cursor.execute(sql, val)
    conn.commit()
    conn.close()
    return {"message": "Student updated successfully"}

@app.delete("/estudiantes/{id}")
def delete_student(id: int):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM estudiantes WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    return {"message": "Student deleted successfully"}
