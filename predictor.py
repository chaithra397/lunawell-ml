from datetime import datetime, timedelta

# Predict next period date
def predict_next_period(last_period_date, cycle_length):
    """
    last_period_date format: YYYY-MM-DD
    cycle_length: integer (example: 28)
    """

    last_date = datetime.strptime(last_period_date, "%Y-%m-%d")
    next_period = last_date + timedelta(days=cycle_length)

    return next_period.strftime("%Y-%m-%d")


# Calculate how many days remaining
def days_remaining(predicted_date):
    today = datetime.today()
    next_date = datetime.strptime(predicted_date, "%Y-%m-%d")

    return (next_date - today).days