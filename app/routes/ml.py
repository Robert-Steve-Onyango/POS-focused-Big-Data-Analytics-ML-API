from fastapi import APIRouter
import pandas as pd
from datetime import datetime
from app.services.sales_forecast import forecast_sales

router = APIRouter()

@router.get("/sales")
def get_sales_forecast():
    result = forecast_sales()
    return result