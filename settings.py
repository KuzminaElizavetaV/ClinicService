from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str
    TEST_DATABASE_URL: str

    class Config:
        env_file = '.env'


settings = Settings()
