from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()  # pragma: no mutate

@app.get("/", response_model=dict)
async def root():
    """
    Root endpoint
    """
    return {"message": "Hello"}

@app.get("/sum", response_model=int)
async def get_sum(a: int, b: int):
    """
    Return the sum of two integers
    """
    return a + b

@app.get("/division", response_model=Optional[float])
async def get_division(dividend: float, divisor: float) -> float:
    """
    Calculates the division of two numbers.

    Args:
        dividend (float): The number to divide.
        divisor (float): The number to divide by.

    Returns:
        float: The result of the division.

    Raises:
        ValueError: If the divisor is zero.
    """
    if divisor == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    else:
        return dividend / divisor