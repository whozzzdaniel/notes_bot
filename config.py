# config.py
from os import getenv
from dotenv import load_dotenv
from dataclasses import dataclass


load_dotenv()


@dataclass
class Settings:
    bot_token: str

def get_settings() -> Settings:
    return Settings(
        bot_token=getenv('BOT_TOKEN', "")
    )


settings = get_settings()