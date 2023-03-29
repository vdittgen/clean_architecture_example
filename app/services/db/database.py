from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.services.db.models import Base


engine = create_engine('sqlite:///example.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
