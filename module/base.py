from sqlalchemy import Column, BigInteger, String
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()


class TokenTable(Base):
    """
    
    Table for token

    """

    __tablename__ = "token"


    user_id = Column(BigInteger, primary_key=True)
    token = Column(String(256), unique=True)


    def __init__(self, user_id : int, token : str):
        self.user_id = user_id
        self.token = token

