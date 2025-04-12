from fastapi import APIRouter
import pandas as pd
from datetime import datetime

router = APIRouter()

@router.get("/sales-summary")
def sales_summary():
    # Placeholder data - replace with DB query
    data = pd.DataFrame({
        "date": pd.date_range(end=datetime.today(), periods=10),
        "sales": [100, 150, 200, 170, 120, 180, 220, 210, 190, 230]
    })
    total = data['sales'].sum()
    average = data['sales'].mean()
    return {"total_sales": total, "average_daily_sales": average}