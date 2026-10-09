"""Convert metrics into a 0-100 Financial Health Score."""
import numpy as np


WEIGHTS = {
    "DTI": 0.25,
    "Expense Ratio": 0.15,
    "Savings Ratio": 0.20,
    "Credit Utilization": 0.20,
    "EMI Ratio": 0.15,
    "Monthly Surplus": 0.05,
}


def _score_dti(v):          return np.clip(100 - (v * 150), 0, 100)
def _score_expense(v):      return np.clip(100 - (v * 100), 0, 100)
def _score_savings(v):      return np.clip(v * 300, 0, 100)
def _score_credit_util(v):  return np.clip(100 - (v * 130), 0, 100)
def _score_emi(v):          return np.clip(100 - (v * 160), 0, 100)
def _score_surplus(v, inc): return np.clip((v / (inc + 1e-6)) * 300, 0, 100)


def compute_health_score(metrics: dict, monthly_income: float) -> dict:
    components = {
        "DTI": _score_dti(metrics["DTI"]),
        "Expense Ratio": _score_expense(metrics["Expense Ratio"]),
        "Savings Ratio": _score_savings(metrics["Savings Ratio"]),
        "Credit Utilization": _score_credit_util(metrics["Credit Utilization"]),
        "EMI Ratio": _score_emi(metrics["EMI Ratio"]),
        "Monthly Surplus": _score_surplus(metrics["Monthly Surplus"], monthly_income),
    }
    total = sum(components[k] * WEIGHTS[k] for k in components)
    score = round(float(total), 1)

    if score >= 70:
        band = "Low Risk"
    elif score >= 45:
        band = "Moderate Risk"
    else:
        band = "High Risk"

    return {"score": score, "band": band, "components": components}