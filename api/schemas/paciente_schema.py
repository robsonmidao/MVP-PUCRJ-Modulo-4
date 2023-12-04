from pydantic import BaseModel
from typing import Optional, List
from model.paciente import Paciente
import json
import numpy as np

class PacienteSchema(BaseModel):
    """ Define como um novo paciente a ser inserido deve ser representado
    """
    name: str = 'Robson'
    age: int = 42
    sex: int = 1
    cp: int = 0
    trestbps: int = 148
    chol: int = 244
    fbs: int = 0
    restecg: int = 2
    thalach: int = 178
    exang: int = 0
    oldpeak: float = 0.8
    slope: int = 0
    ca: int = 2
    thal: int = 0
    
class PacienteViewSchema(BaseModel):
    """Define como um paciente será retornado
    """
    id: int = 1
    name: str = 'Robson'
    age: int = 35
    sex: int = 1
    cp: int = 1
    trestbps: int = 100
    chol: int = 120
    fbs: int = 1
    restecg: int = 2
    thalach: int = 170
    exang: int = 1
    oldpeak: float = 1.7
    slope: int = 1
    ca: int = 1
    thal: int = 2
    condition: int = None

    
class PacienteBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do paciente.
    """
    name: str = "Robson"

class ListaPacientesSchema(BaseModel):
    """Define como uma lista de pacientes será representada
    """
    pacientes: List[PacienteSchema]

    
class PacienteDelSchema(BaseModel):
    """Define como um paciente para deleção será representado
    """
    name: str = "Robson"
    
# Apresenta apenas os dados de um paciente    
def apresenta_paciente(paciente: Paciente):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    return {
        "id": paciente.id,
        "name": paciente.name,
        "age": paciente.age,
        "sex":  paciente.sex,
        "cp":  paciente.cp,
        "trestbps":  paciente.trestbps,
        "chol":  paciente.chol,
        "fbs":  paciente.fbs,
        "restecg":  paciente.restecg,
        "thalach":  paciente.thalach,
        "exang":  paciente.exang,
        "oldpeak":  paciente.oldpeak,
        "slope":  paciente.slope,
        "ca":  paciente.ca,
        "thal":  paciente.thal,
        "condition":  paciente.condition
    }
    
# Apresenta uma lista de pacientes
def apresenta_pacientes(pacientes: List[Paciente]):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    result = []
    for paciente in pacientes:
        result.append({
            "id": paciente.id,
            "name": paciente.name,
            "age": paciente.age,
            "sex":  paciente.sex,
            "cp":  paciente.cp,
            "trestbps":  paciente.trestbps,
            "chol":  paciente.chol,
            "fbs":  paciente.fbs,
            "restecg":  paciente.restecg,
            "thalach":  paciente.thalach,
            "exang":  paciente.exang,
            "oldpeak":  paciente.oldpeak,
            "slope":  paciente.slope,
            "ca":  paciente.ca,
            "thal":  paciente.thal,
            "condition":  paciente.condition
        })

    return {"pacientes": result}

