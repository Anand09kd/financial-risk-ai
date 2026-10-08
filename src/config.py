"""Central configuration for the platform."""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# ---------- Paths ----------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_RAW = BASE_DIR / "data" / "raw"
DATA_PROCESSED = BASE_DIR / "data" / "processed"
UPLOADS_DIR = BASE_DIR / "data" / "uploads"
POLICY_DOCS_DIR = BASE_DIR / "data" / "policy_docs"
MODELS_DIR = BASE_DIR / "models"
MODEL_PATH = MODELS_DIR / "risk_classifier.pkl"
VECTOR_STORE_PATH = BASE_DIR / "vector_store"

for p in [DATA_RAW, DATA_PROCESSED, UPLOADS_DIR, POLICY_DOCS_DIR,
          MODELS_DIR, VECTOR_STORE_PATH]:
    p.mkdir(parents=True, exist_ok=True)

# ---------- ML ----------
RANDOM_STATE = 42
TEST_SIZE = 0.2
N_ESTIMATORS = 200
MAX_DEPTH = 5
LEARNING_RATE = 0.05
RISK_LABELS = ["Low Risk", "Moderate Risk", "High Risk"]

# ---------- RAG ----------
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
CHUNK_SIZE = 512
CHUNK_OVERLAP = 50
TOP_K_RETRIEVAL = 4

# ---------- LLM ----------
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "gemini")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")

# ---------- Anomaly ----------
ANOMALY_Z_THRESHOLD = 2.5
ANOMALY_WINDOW = 3

# ---------- API ----------
API_HOST = "0.0.0.0"
API_PORT = 8000