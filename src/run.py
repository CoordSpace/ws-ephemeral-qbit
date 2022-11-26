"""
Module that run the setup for windscrib's ephemeral port
"""
import time
import schedule

from logger import create_logger
from util import to_seconds
from ws import reset_ephemeral_port

# wait befor setting the ephemeral ports
DAYS: int = 6

logger = create_logger("run")

while True:
    logger.info("Setting the ephemeral port & starting schedule")
    reset_ephemeral_port()
    schedule.every(DAYS).days.do(reset_ephemeral_port)

    while 1:
        n = schedule.idle_seconds()
        if n is None:
            # no more jobs
            logger.info("No jobs found, something is probably wrong!")
            break
        elif n > 0:
            logger.info("Going to wait patiently for %s seconds before next reset", n)
            # sleep exactly the right amount of time
            time.sleep(n)
        schedule.run_pending()
