import databases
import sqlalchemy as sa

DATABASE_URL = "sqlite:///./pythagoras.db"

database = databases.Database(DATABASE_URL)

metadata = sa.MetaData()

about_info = sa.Table(
    "about_info",
    metadata,
    sa.Column("name", sa.String, primary_key=True),
    sa.Column("info_rus", sa.String),
    sa.Column("info_en", sa.String),
    sa.Column("info_de", sa.String),
    sa.Column("info_ua", sa.String),
)

engine = sa.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

