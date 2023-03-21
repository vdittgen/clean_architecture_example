from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base

engine = create_engine('redis://localhost:6379/0')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
