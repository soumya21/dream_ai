# app/core/config.py
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

class Settings(BaseSettings):
    jwt_secret_key: str = os.getenv("JWT_SECRET_KEY")
    dynamodb_region: str = os.getenv("DYNAMODB_REGION")
    dynamodb_table: str = os.getenv("DYNAMODB_TABLE")
    api_key: str = os.getenv("API_KEY")
    agent_id: str = os.getenv("AGENT_ID")
    alias_id: str = os.getenv("ALIAS_ID")
    bedrock_agent_region: str =os.getenv("BEDROCK_AGENT_REGION")
    aws_access_key_id: str = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key: str = os.getenv("AWS_SECRET_ACCESS_KEY")
    db_user: str = os.getenv("DB_USER")
    db_password: str = os.getenv("DB_PASSWORD")
    db_host: str = os.getenv("DB_HOST")
    db_port: str = os.getenv("DB_PORT")
    db_name: str = os.getenv("DB_NAME")

    class Config:
        env_file = ".env"

settings = Settings()
