from decouple import config

class Settings:
    
    ## Email MCP Tool
    SENDER_EMAIL : str = config("SENDER_EMAIL")
    PASSWORD = config("PASSWORD")
    
    ## JWT Authentication
    JWT_ALGORITHM = config("JWT_ALGORITHM")
    JWT_SECRET = config("JWT_SECRET")
    JWT_ISSUER = config("JWT_ISSUER")
    JWT_EXPIRE_HOURS: int = config("JWT_EXPIRE_HOURS")
    JWT_AUDIENCE:str = config("JWT_AUDIENCE")
    
    
setting = Settings()