import pandas as pd
from prophet import Prophet
from datetime import datetime

# Dummy data
sales_data = pd.DataFrame({
    "ds": pd.date_range(end=datetime.today(), periods=30),
    "y": [100 + i * 2 + (i % 5) * 5 for i in range(30)]
})

def forecast_sales():
    model = Prophet()
    model.fit(sales_data)
    future = model.make_future_dataframe(periods=7)
    forecast = model.predict(future)
    result = forecast[['ds', 'yhat']].tail(7).to_dict(orient="records")
    return {"forecast_next_7_days": result}