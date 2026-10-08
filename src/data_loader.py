"""Load raw datasets and policy documents."""
import pandas as pd
from pathlib import Path
from src.config import DATA_RAW, POLICY_DOCS_DIR


def load_loan_data() -> pd.DataFrame:
    """Load and concatenate all CSVs in data/raw."""
    csv_files = list(Path(DATA_RAW).glob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in {DATA_RAW}")

    dfs = [pd.read_csv(f) for f in csv_files]
    combined = pd.concat(dfs, ignore_index=True) if len(dfs) > 1 else dfs[0]
    print(f"[data_loader] Loaded {len(combined)} rows × {combined.shape[1]} cols")
    return combined


def load_policy_documents() -> list[str]:
    """Load TXT / PDF policy documents for RAG."""
    docs = []
    for file in Path(POLICY_DOCS_DIR).glob("*"):
        if file.suffix.lower() == ".txt":
            docs.append(file.read_text(encoding="utf-8"))
        elif file.suffix.lower() == ".pdf":
            try:
                import pdfplumber
                with pdfplumber.open(file) as pdf:
                    text = "\n".join((p.extract_text() or "") for p in pdf.pages)
                    docs.append(text)
            except Exception as e:
                print(f"[data_loader] Skipped {file.name}: {e}")
    print(f"[data_loader] Loaded {len(docs)} policy documents")
    return docs