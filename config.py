import os

class Config:
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///default.db')
    EMAIL_SERVICE_HOST = os.getenv('EMAIL_SERVICE_HOST', 'smtp.example.com')
    EMAIL_SERVICE_PORT = os.getenv('EMAIL_SERVICE_PORT', 587)
    EMAIL_SERVICE_USER = os.getenv('EMAIL_SERVICE_USER', 'user@example.com')
    EMAIL_SERVICE_PASSWORD = os.getenv('EMAIL_SERVICE_PASSWORD', 'password')