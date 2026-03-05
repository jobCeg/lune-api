from fastapi import Request, HTTPException, status
from datetime import datetime, timedelta
from collections import defaultdict

# Max attempts allowed
MAX_ATTEMPTS = 5

# Time window (minutes)
WINDOW_MINUTES = 1

# { ip: [datetime, datetime, ...] }
login_attempts = defaultdict(list)


def rate_limit_login(request: Request):
    client_ip = request.client.host
    now = datetime.utcnow()

    # Remove old attempts outside the window
    window_start = now - timedelta(minutes=WINDOW_MINUTES)
    login_attempts[client_ip] = [
        attempt for attempt in login_attempts[client_ip]
        if attempt > window_start
    ]

    if len(login_attempts[client_ip]) >= MAX_ATTEMPTS:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many login attempts. Please try again later."
        )

    # Register this attempt
    login_attempts[client_ip].append(now)

