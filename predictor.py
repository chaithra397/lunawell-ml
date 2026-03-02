from datetime import datetime, timedelta

# Predict next period date
def predict_next_period(last_period_date, cycle_length):
    last_date = datetime.strptime(last_period_date, "%Y-%m-%d").date()
    next_period = last_date + timedelta(days=cycle_length)
    return next_period.strftime("%Y-%m-%d")

# Calculate how many days remaining
def days_remaining(predicted_date):
    today = datetime.today().date()  
    next_date = datetime.strptime(predicted_date, "%Y-%m-%d").date()

    return (next_date - today).days




