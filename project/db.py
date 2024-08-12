from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, ForeignKey, Float
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base, relationship

engine = create_engine("sqlite:///blog.sqlite")

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    description = Column(String(255), nullable=False)
    type = Column(String(10), nullable=False)
    amount = Column(Float, nullable=False)

    def __init__(self, date, type, amount, description=None):
        self.date = date
        self.description = description
        self.type = type
        self.amount = amount

    def __repr__(self):
        return f"<Transaction {self.date} {self.description} {self.type} {self.amount}>"


if __name__ == "__main__":
    Base.metadata.create_all(engine)
