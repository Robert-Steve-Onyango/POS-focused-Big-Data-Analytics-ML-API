from fastapi import FastAPI
from app.routes import upload, analytics, ml

app = FastAPI(title="POS Analytics & ML API")

app.include_router(upload.router, prefix="/upload")
app.include_router(analytics.router, prefix="/analytics")
app.include_router(ml.router, prefix="/predict")