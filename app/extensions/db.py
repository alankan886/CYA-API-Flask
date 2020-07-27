from flask_sqlalchemy import SQLAlchemy as SQLAlchemyBase
from sqlalchemy import MetaData
from sqlalchemy.pool import NullPool, QueuePool

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

class SQLAlchemy(SQLAlchemyBase):
    def apply_driver_hacks(self, app, info, options):
        super(SQLAlchemy, self).apply_driver_hacks(app, info, options)
        options['poolclass'] = NullPool
        options.pop('pool_size', None)

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata, engine_options={"pool_size": 10, "poolclass":QueuePool, "pool_pre_ping":True})