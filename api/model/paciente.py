from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

# colunas = name,age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,condition

class Paciente(Base):
    __tablename__ = 'pacientes'
    
    id = Column(Integer, primary_key=True)
    name = Column("name", String(50))
    age = Column("age", Integer)
    sex = Column("sex", Integer)
    cp = Column("cp", Integer)
    trestbps = Column("trestbps", Integer)
    chol = Column("chol", Integer)
    fbs = Column("fbs", Integer)
    restecg = Column("restecg", Integer)
    thalach = Column("thalach", Integer)
    exang = Column("exang", Integer)
    oldpeak = Column("oldpeak", Float)
    slope = Column("slope", Integer)
    ca = Column("ca", Integer)
    thal = Column("thal", Integer)
    condition = Column("condition", Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())
    
    def __init__(self, name:str, age:int, sex:int, cp:int, trestbps:str,
                 chol:int, fbs:int, restecg:int, 
                 thalach:float, exang:int, oldpeak:int, slope:int, ca:int, thal:int, condition:int, 
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Paciente

        Arguments:
            age: age in years
            name: pacient name
            sex: sex (1 = male; 0 = female)
            cp: chest pain type
            -- Value 0: typical angina
            -- Value 1: atypical angina
            -- Value 2: non-anginal pain
            -- Value 3: asymptomatic
            trestbps: resting blood pressure (in mm Hg on admission to the hospital)
            chol: serum cholestoral in mg/dl
            fbs: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
            restecg: resting electrocardiographic results
            -- Value 0: normal
            -- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
            -- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria
            thalach: maximum heart rate achieved
            exang: exercise induced angina (1 = yes; 0 = no)
            oldpeak = ST depression induced by exercise relative to rest
            slope: the slope of the peak exercise ST segment
            -- Value 0: upsloping
            -- Value 1: flat
            -- Value 2: downsloping
            ca: number of major vessels (0-3) colored by flourosopy
            thal: 0 = normal; 1 = fixed defect; 2 = reversable defect
            and the label
            condition: 0 = no disease, 1 = disease
        """
        self.name = name
        self.age = age
        self.sex = sex
        self.cp = cp
        self.trestbps = trestbps
        self.chol = chol
        self.fbs = fbs
        self.restecg = restecg
        self.thalach = thalach
        self.exang = exang
        self.oldpeak = oldpeak
        self.slope = slope
        self.ca = ca
        self.thal = thal
        self.condition= condition

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao