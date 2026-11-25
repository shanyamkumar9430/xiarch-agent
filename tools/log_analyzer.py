
# Login security log analyzer

LOGIN_LOGS = [
    {
        "username": "admin",
        "ip": "185.220.101.1",
        "status": "failed",
        "time": "02:15 AM"
    },
    {
        "username": "admin",
        "ip": "185.220.101.1",
        "status": "failed",
        "time": "02:16 AM"
    },
    {
        "username": "admin",
        "ip": "185.220.101.1",
        "status": "failed",
        "time": "02:17 AM"
    },
    {
        "username": "sayam",
        "ip": "8.8.8.8",
        "status": "success",
        "time": "10:30 AM"
    }
]


def analyze_login_logs(username: str = None) -> dict:
    """Analyze simulated login events."""

    if username:
        events = [
            log for log in LOGIN_LOGS
            if log["username"].lower() == username.lower()
        ]
    else:
        events = LOGIN_LOGS.copy()

    failed = sum(
        1 for event in events
        if event["status"] == "failed"
    )

    successful = sum(
        1 for event in events
        if event["status"] == "success"
    )

    return {
        "username": username or "all users",
        "total_events": len(events),
        "failed_logins": failed,
        "successful_logins": successful,
        "events": events,
        "source": "Simulated login database"
    }
