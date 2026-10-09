"""Compute the 6 key financial metrics shown on the dashboard."""
import pandas as pd


METRIC_DESCRIPTIONS = {
    "DTI": "Debt-to-Income Ratio — how much you owe vs earn",
    "Expense Ratio": "Expense Ratio — % of income spent monthly",
    "Savings Ratio": "Savings Ratio — % of income saved",
    "Credit Utilization": "Credit Utilization — % of credit limit used",
    "EMI Ratio": "EMI Ratio — share of income going to EMIs",
    "Monthly Surplus": "Monthly Surplus — money left after expenses & EMIs",
}


def compute_metrics(profile_df: pd.DataFrame) -> dict:
    row = profile_df.iloc[0]
    return {
        "DTI": float(row["dti_ratio"]),
        "Expense Ratio": float(row["expense_ratio"]),
        "Savings Ratio": float(row["savings_ratio"]),
        "Credit Utilization": float(row["credit_utilization"]),
        "EMI Ratio": float(row["emi_ratio"]),
        "Monthly Surplus": float(row["monthly_surplus"]),
    }


def metric_status(metric_name: str, value: float) -> str:
    rules = {
        "DTI":                [(0.36, "Good"), (0.50, "Warning"), (float("inf"), "Poor")],
        "Expense Ratio":      [(0.50, "Good"), (0.75, "Warning"), (float("inf"), "Poor")],
        "Savings Ratio":      [(0.20, "Good"), (0.10, "Warning"), (float("-inf"), "Poor")],
        "Credit Utilization": [(0.30, "Good"), (0.50, "Warning"), (float("inf"), "Poor")],
        "EMI Ratio":          [(0.30, "Good"), (0.50, "Warning"), (float("inf"), "Poor")],
        "Monthly Surplus":    [(0.20, "Good"), (0.0, "Warning"), (float("-inf"), "Poor")],
    }
    inverted = metric_name in ("Savings Ratio", "Monthly Surplus")
    for threshold, label in rules[metric_name]:
        if inverted:
            if value >= threshold:
                return label
        else:
            if value < threshold:
                return label
    return "Unknown"