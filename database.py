from sqlalchemy import create_engine, text

# Passando o argumento connect_args corretamente
engine = create_engine(
    "mysql+pymysql://root:TTbKmbOVNiOvdwLGmspdijnKnxwmnFRS@junction.proxy.rlwy.net:42657/railway?charset=utf8mb4",
    connect_args={"connect_timeout": 60}
)

def carrega_vagas_db():
    with engine.connect() as conn:
        resultado = conn.execute(text("select * from vagas"))
        vagas = []
        for vaga in resultado.all():
            vagas.append(vaga._asdict()) # adicionado em uma lista os dados como dicionario utilizando o _asdict()
        return vagas


