from cmath import log
from os import getenv
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(".") / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "API EDUCAR Cibercolegios"
    PROJECT_VERSION: str = "1.0"
    DB_HOST: str = getenv("DB_HOST")
    DB_USER: str = getenv("DB_USER")
    DB_PASS: str = getenv("DB_PASS")
    DB_PORT: str = getenv("DB_PORT")
    DB: str = getenv("DB_DATABASE")
    AWS_ACCESS_KEY_ID: str = getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: str = getenv("AWS_SECRET_ACCESS_KEY")
    AWS_REGION_NAME: str = getenv("AWS_REGION_NAME")

    # sesion = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_REGION_NAME)


settings = Settings()
