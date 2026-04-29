from __future__ import annotations

from pydantic import BaseModel, Field


class EntityBlock(BaseModel):
    organizations: list[str] = []
    dates: list[str] = []
    amounts: list[str] = []
    invoice_ids: list[str] = []


class DocumentRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Business document text input")


class DocumentResponse(BaseModel):
    summary: str
    key_entities: EntityBlock
    risk_flags: list[str]
    action_items: list[str]
    confidence_score: str
