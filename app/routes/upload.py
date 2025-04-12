from fastapi import APIRouter, UploadFile, File
import pandas as pd
from io import StringIO

router = APIRouter()

@router.post("/sales-data")
def upload_sales_data(file: UploadFile = File(...)):
    content = file.file.read().decode("utf-8")
    df = pd.read_csv(StringIO(content))
    # You would typically store this to a database here
    return {"rows_received": len(df), "columns": list(df.columns)}