import qbittorrentapi
import config
from logger import create_logger
from time import sleep

class Qbit:
    def __init__(self) -> None:
        self.logger = create_logger("qbit")
        self.client = \
            qbittorrentapi.Client(host=config.QBHOST, port=config.QBPORT, username=config.QBUSERNAME, password=config.QBPASSWORD)
        pass

    def login(self) -> None:
        self.logger.debug("Attempting to log in to qbittorrent...")
        try:
            self.client.auth_log_in()
        except qbittorrentapi.LoginFailed as e:
            self.logger.error(e)
            print(e)
            pass
        self.logger.debug("Logged into qbittorrent!")

    def set_port(self, port) -> None:
        self.logger.info("Setting port in qbittorrent.")
        self.client.app_set_preferences(prefs={'listen_port': port})
        # Wait a bit for the config change to settle
        sleep(1)
        prefs = self.client.app_preferences()

        self.logger.debug(("Listen port from config: {0}".format(prefs['listen_port'])))

        if prefs['listen_port'] != port:
            self.logger.error("Port is not set!")

def set_qbit_port(port) -> None:
    q = Qbit()
    q.login()
    q.set_port(port)