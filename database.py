from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()
# Passando o argumento connect_args corretamente

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4",
    connect_args={"connect_timeout": 60}
)

def carrega_vagas_db():
    with engine.connect() as conn:
        resultado = conn.execute(text("select * from vagas"))
        vagas = []
        for vaga in resultado.all():
            vagas.append(vaga._asdict()) # adicionado em uma lista os dados como dicionario utilizando o _asdict()
        return vagas

def carrega_vaga(id):
    with engine.connect() as conn:
        resultado = conn.execute(text(f"select * from vagas where id =  :val"),{"val":id})
        registro = resultado.mappings().all()
        if len(registro) == 0:
            return None
        else:
            return dict(registro[0])



