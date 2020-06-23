from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.pool import NullPool
from config import SQLALCHEMY_DATABASE_URI

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    poolclass=NullPool
)

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)