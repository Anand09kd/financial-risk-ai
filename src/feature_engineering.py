"""Compute all financial ratios used by the model."""
import pandas as pd


EPS = 1e-6


def compute_ratios(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["dti_ratio"] = df["total_debt"] / (df["monthly_income"] * 12 + EPS)
    df["expense_ratio"] = df["monthly_expenses"] / (df["monthly_income"] + EPS)
    df["savings_ratio"] = (
        (df["monthly_income"] - df["monthly_expenses"] - df["monthly_emi"])
        / (df["monthly_income"] + EPS)
    )
    df["credit_utilization"] = df["credit_used"] / (df["credit_limit"] + EPS)
    df["emi_ratio"] = df["monthly_emi"] / (df["monthly_income"] + EPS)
    df["monthly_surplus"] = (
        df["monthly_income"] - df["monthly_expenses"] - df["monthly_emi"]
    )
    df["loan_to_income"] = df["num_active_loans"] / (df["monthly_income"] / 10000 + EPS)
    return df


def get_feature_columns() -> list[str]:
    return [
        "monthly_income", "monthly_expenses", "monthly_emi",
        "num_active_loans", "total_debt", "total_savings",
        "credit_limit", "credit_used",
        "dti_ratio", "expense_ratio", "savings_ratio",
        "credit_utilization", "emi_ratio", "monthly_surplus",
        "loan_to_income",
    ]