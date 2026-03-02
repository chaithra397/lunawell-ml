from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from predictor import predict_next_period, days_remaining

app = FastAPI()
class PeriodData(BaseModel):
    lastPeriodDate: str
    cycleLength: int
origins = [
    "http://localhost:9002",
    "http://127.0.0.1:9002",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "LunaWell ML server running"}

@app.post("/predict")
def predict(data: PeriodData):

    # Get predicted next period date
    next_period = predict_next_period(
        data.lastPeriodDate,
        data.cycleLength
    )

    # Calculate days remaining
    remaining_days = days_remaining(next_period)

    # Recommendation logic
    if remaining_days < 0:
        recommendation = "Your cycle date has passed. Please update your last period date."
    elif remaining_days == 0:
        recommendation = "Your cycle may start today. Take rest and stay prepared."
    elif remaining_days <= 3:
        recommendation = "Your period is approaching. Take rest and stay hydrated."
    else:
        recommendation = "Your cycle is regular. Maintain a healthy lifestyle."

    return {
        "nextPeriodDate": next_period,
        "daysRemaining": remaining_days,
        "recommendation": recommendation
    }