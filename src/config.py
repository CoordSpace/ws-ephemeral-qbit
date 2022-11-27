"""
config module
"""
import os
import sys
from typing import Optional

import httpx

from dotenv import load_dotenv

from util import validate_port

# Load a development .env file if available
load_dotenv()

# common config
CSRF_URL: str = "https://res.windscribe.com/res/logintoken"

BASE_URL: str = "https://windscribe.com/"
LOGIN_URL: str = BASE_URL + "login"
MYACT_URL: str = BASE_URL + "myaccount"

STATICIP: str = BASE_URL + "staticips/"
EPHEM_URL: str = STATICIP + "load"
DEL_EPHEM_URL: str = STATICIP + "deleteEphPort"
SET_EPHEM_URL: str = STATICIP + "postEphPort"

DEBUG: bool = bool(os.environ.get("WS_DEBUG"))

USERNAME: Optional[str] = os.environ.get("WS_USERNAME")
PASSWORD: Optional[str] = os.environ.get("WS_PASSWORD")
TOTP_TOKEN: Optional[str] = os.environ.get("WS_TOTP_TOKEN")

QBUSERNAME: Optional[str] = os.environ.get("QB_USERNAME")
QBPASSWORD: Optional[str] = os.environ.get("QB_PASSWORD")
QBPORT: int = validate_port(os.environ.get("QB_PORT"))
QBHOST: Optional[str] = os.environ.get("QB_HOST")

if not all([USERNAME, PASSWORD, QBUSERNAME, QBPASSWORD, QBPORT, QBHOST]):
    print("Environment variables: Usernames, passwords, ports, and host are all required.")
    sys.exit(1)

# some HTML id for the login purpose
# TODO: expose via config file
USERNAME_ID: str = "username"
PASSWORD_ID: str = "password"

COOKIES = httpx.Cookies()
COOKIES.set("i_can_has_cookie", "1")
COOKIES.set("ref", "https://windscribe.com/")
