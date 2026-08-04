from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

AZURE_API_KEY = os.getenv("AZURE_API_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
MODEL_NAME = os.getenv("MODEL_NAME")
API_VERSION = os.getenv("API_VERSION")
print("ENV PATH :", BASE_DIR / ".env")
print("ENV EXISTS :", (BASE_DIR / ".env").exists())
print("MODEL VALUE :", MODEL_NAME)