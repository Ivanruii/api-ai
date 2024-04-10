from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from ..core.ai import calculate_differences

router = APIRouter()

class InputSentences(BaseModel):
    sentences: List[str]

class OutputDifferences(BaseModel):
    differences: List[float]

@router.post("/calculate_differences/", response_model=OutputDifferences)
async def calculate_differences_api(input_data: InputSentences):
    sentences = input_data.sentences
    if len(sentences) < 2:
        raise HTTPException(status_code=400, detail="At least two sentences must be provided")
    differences = calculate_differences(sentences)
    return {"differences": differences}
