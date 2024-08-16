from dataclasses import dataclass
from environs import Env 


@dataclass
class Config:
    bot_token: str
    path: str

env: Env = Env()

env.read_env()

config = Config(
    bot_token=env('BOT_TOKEN'),
    path=env('path')
)