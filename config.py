import os

class Config:
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or '1017'
    DB_HOST = os.environ.get('DB_HOST') or 'localhost'
    DB_NAME = os.environ.get('DB_NAME') or 'employeeapi'
    DB_USER = os.environ.get('DB_USER') or 'postgres'
    DB_PASSWORD = os.environ.get('DB_PASSWORD') or '1017'