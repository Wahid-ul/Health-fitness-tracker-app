import os

class Config:
    SECRET_KEY=os.getenv('SECRET_KEY','my_secret_key')
    SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URI','postgresql://postgres:Wahidul123@localhost/health_fitness_db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    JWT_SECRET_KEY=os.getenv('JWT_SECRET_KEY','superjwtsecretkey')
    