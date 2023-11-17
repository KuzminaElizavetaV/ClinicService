import databases
import sqlalchemy
from settings import settings

DATABASE_URL = settings.DATABASE_URL
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

clients = sqlalchemy.Table(
    "clients",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("document", sqlalchemy.String(50), nullable=False),
    sqlalchemy.Column("surname", sqlalchemy.String(30), nullable=False),
    sqlalchemy.Column("firstname", sqlalchemy.String(30), nullable=False),
    sqlalchemy.Column("patronymic", sqlalchemy.String(30), nullable=True),
    sqlalchemy.Column("birthday", sqlalchemy.Date, nullable=False),
    sqlalchemy.Column("phone", sqlalchemy.BigInteger, nullable=False),
    sqlalchemy.Column("email", sqlalchemy.String(50), unique=True, nullable=False),
)

pets = sqlalchemy.Table(
    "pets",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(50), nullable=False),
    sqlalchemy.Column("birthday", sqlalchemy.Date, nullable=False),
    sqlalchemy.Column("client_id", sqlalchemy.ForeignKey("clients.id"), nullable=False),
)


consultations = sqlalchemy.Table(
    "consultations",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("consultation_date", sqlalchemy.Date, nullable=False),
    sqlalchemy.Column("client_id", sqlalchemy.ForeignKey("clients.id"), nullable=False),
    sqlalchemy.Column("pet_id", sqlalchemy.ForeignKey("pets.id"), nullable=False),
    sqlalchemy.Column("description", sqlalchemy.String(300), nullable=False),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)
