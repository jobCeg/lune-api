from datetime import datetime
from app.utils.appointments import compute_appointment_end_time


def test_compute_end_time_30_minutes():
    start = datetime(2026, 3, 4, 10, 0, 0)
    end = compute_appointment_end_time(start, 30)

    assert end == datetime(2026, 3, 4, 10, 30, 0)


def test_compute_end_time_60_minutes():
    start = datetime(2026, 3, 4, 9, 0, 0)
    end = compute_appointment_end_time(start, 60)

    assert end == datetime(2026, 3, 4, 10, 0, 0)


def test_compute_end_time_90_minutes():
    start = datetime(2026, 3, 4, 8, 0, 0)
    end = compute_appointment_end_time(start, 90)

    assert end == datetime(2026, 3, 4, 9, 30, 0)
