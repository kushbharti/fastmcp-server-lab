from decouple import config

class Settings:
    
    ## Email MCP Tool
    SENDER_EMAIL : str = config("SENDER_EMAIL")
    PASSWORD = config("PASSWORD")
    
    ## JWT Authentication
    JWT_ALGORITHM = config("JWT_ALGORITHM")
    JWT_SECRET = config("JWT_SECRET")
    JWT_ISSUER = config("JWT_ISSUER")
    JWT_EXPIRE_HOURS: int = config("JWT_EXPIRE_HOURS", cast=int)
    JWT_AUDIENCE:str = config("JWT_AUDIENCE")
    
    # Google Oauth Authentication
    GOOGLE_CLIENT_ID:str = config("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET:str = config("GOOGLE_CLIENT_SECRET")
    
    MCP_SERVER_URL:str =config("MCP_SERVER_URL")
setting = Settings()