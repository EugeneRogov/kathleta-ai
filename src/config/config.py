import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        
        self.model_path = os.getenv("MODEL_PATH", "models/")
        self.data_path = os.getenv("DATA_PATH", "data/")
        self.api_key = os.getenv("API_KEY", "")
        self.api_host = os.getenv("API_HOST", "0.0.0.0")
        self.api_port = int(os.getenv("API_PORT", "5000"))
        self.api_debug = os.getenv("API_DEBUG", "True").lower() == "true"
