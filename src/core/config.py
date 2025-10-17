import os
from dotenv import load_dotenv
from dataclasses import dataclass
from typing import Dict

@dataclass
class Config:
    # Параметры ИИ модели
    model_params: Dict = None
    
    # Пути к данным
    data_path: str = "data/"
    model_path: str = "models/"
    
    # Параметры API
    api_host: str = "localhost"
    api_port: int = 8000
