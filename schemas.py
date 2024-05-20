from pydantic import BaseModel
from datetime import date

class Student(BaseModel):
    nombre: str
    apellido: str
    fecha_de_nacimiento: date

class Item(BaseModel):  # Si necesitas esta clase para otros propósitos, la dejo aquí.
    name: str
    age: int
