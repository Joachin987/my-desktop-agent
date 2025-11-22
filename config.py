from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "My Desktop Agent"
    version: str = "1.0"
    debug: bool = False
    api_key: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()