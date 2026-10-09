"""Input validation using Pydantic."""
from pydantic import BaseModel, Field, field_validator


class FinancialProfile(BaseModel):
    monthly_income: float = Field(..., gt=0)
    monthly_expenses: float = Field(..., ge=0)
    monthly_emi: float = Field(..., ge=0)
    num_active_loans: int = Field(..., ge=0, le=50)
    total_debt: float = Field(..., ge=0)
    total_savings: float = Field(..., ge=0)
    credit_limit: float = Field(..., ge=0)
    credit_used: float = Field(..., ge=0)

    @field_validator("credit_used")
    @classmethod
    def used_le_limit(cls, v, info):
        limit = info.data.get("credit_limit")
        if limit is not None and v > limit:
            raise ValueError("credit_used cannot exceed credit_limit")
        return v


def validate_input(data: dict) -> FinancialProfile:
    return FinancialProfile(**data)