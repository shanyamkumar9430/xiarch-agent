
# Simulated IP intelligence tool
# Uses sample data for safe project testing.

IP_DATABASE = {
    "185.220.101.1": {
        "country": "Unknown",
        "risk_level": "High",
        "category": "Known suspicious source (simulated)",
    },
    "8.8.8.8": {
        "country": "United States",
        "risk_level": "Low",
        "category": "Public DNS server (simulated)",
    },
}


def lookup_ip(ip_address: str) -> dict:
    """Retrieve simulated intelligence about an IP address."""

    result = IP_DATABASE.get(ip_address)

    if result:
        return {
            "ip_address": ip_address,
            "found": True,
            "intelligence": result,
            "source": "Simulated project database",
        }

    return {
        "ip_address": ip_address,
        "found": False,
        "message": "No information found in the simulated database.",
        "source": "Simulated project database",
    }
