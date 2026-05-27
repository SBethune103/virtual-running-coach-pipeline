import os
from pathlib import Path
from dotenv import load_dotenv
import yaml

# Load environment variables from .env
load_dotenv()

# Base directory
BASE_DIR = Path(__file__).parent.parent.parent

class Settings:
    def __init__(self):
        # Load config.yaml
        config_path = BASE_DIR / "config.yaml"
        with open(config_path, encoding="utf-8") as f:
            self.config = yaml.safe_load(f)
        
        # Strava credentials from .env (preferred over config.yaml)
        self.strava_client_id = os.getenv("STRAVA_CLIENT_ID")
        self.strava_client_secret = os.getenv("STRAVA_CLIENT_SECRET")
        
        # Paths
        self.raw_data_path = BASE_DIR / self.config["paths"]["raw_data"]
        self.processed_data_path = BASE_DIR / self.config["paths"]["processed_data"]
        self.vector_db_path = BASE_DIR / self.config["paths"]["vector_db"]
        
        # Ensure directories exist
        self.raw_data_path.mkdir(parents=True, exist_ok=True)
        self.processed_data_path.mkdir(parents=True, exist_ok=True)
        self.vector_db_path.mkdir(parents=True, exist_ok=True)

    @property
    def embedding_model(self):
        return self.config["embedding"]["model_name"]
    
    @property
    def chunk_size(self):
        return self.config["embedding"]["chunk_size"]
    
    @property
    def chunk_overlap(self):
        return self.config["embedding"]["chunk_overlap"]

# Create global settings instance
settings = Settings()