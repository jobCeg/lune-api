from datetime import datetime, timedelta


def compute_appointment_end_time(start_time: datetime, duration_minutes: int) -> datetime:
    """
    Compute the end time of an appointment given the start time
    and the service duration in minutes.
    """

    if duration_minutes <= 0:
        raise ValueError("Duration must be greater than 0")

    return start_time + timedelta(minutes=duration_minutes)
