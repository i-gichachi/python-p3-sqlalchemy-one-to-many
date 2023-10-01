from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    genre = Column(String, nullable=False)
    platform = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    # Define the one-to-many relationship between Game and Review
    reviews = relationship('Review', backref='game', lazy='dynamic')

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, autoincrement=True)
    score = Column(Integer, nullable=False)
    comment = Column(String, nullable=True)
    
    # Define the foreign key to establish the relationship
    game_id = Column(Integer, ForeignKey('games.id'), nullable=False)

    def __init__(self, score, comment, game_id):
        self.score = score
        self.comment = comment
        self.game_id = game_id
