from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from predictor import predict_next_period, days_remaining

app = FastAPI()
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
def predict(data: dict):
    last_period = data["lastPeriodDate"]
    cycle_length = int(data["cycleLength"])

    next_date = predict_next_period(last_period, cycle_length)
    remaining = days_remaining(next_date)

    return {
        "nextPeriodDate": next_date,
        "daysRemaining": remaining
    }