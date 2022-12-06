"""
Collection of some helper function for the main program
"""
from typing import Optional

import pyotp


def validate_port(value: Optional[str]) -> int:
    """Just a quick check/convert of the port, used for local qbit instance"""
    if value is None:
        raise ValueError("Valid port number is required")

    port = int(value.strip())

    return port


def to_seconds(days: int) -> int:
    """converts number of day to seconds"""
    return days * 24 * 3600


def get_totp(totp_key: str) -> str:
    """Return current OPT based on TOTP token"""
    totp = pyotp.TOTP(totp_key)
    return totp.now()
    