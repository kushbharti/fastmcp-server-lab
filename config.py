from decouple import config

class Settings:
    
    # Email MCP Tool
    SENDER_EMAIL : str = config("SENDER_EMAIL")
    PASSWORD = config("PASSWORD")
    JWT_ALGORITHM = config("JWT_ALGORITHM")
    JWT_SECRET = config("JWT_SECRET")
    
setting = Settings()