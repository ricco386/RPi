
import logging

LOGFORMAT = '%(asctime)s %(levelname)-8s %(name)s: %(message)s'
logger = logging.getLogger(__name__)

class Client():

    def __init__(self, logfile):
        # Prepare logging configuration
        logconfig = {
            'level': logging.DEBUG,
            'format': LOGFORMAT,
            'filename': logfile
        }

        # Setup logging
        logging.basicConfig(**logconfig)

    def alert(self, message, event = None):
        logger.error(message)

    def notify(self, message, event = None):
        logger.info(message)

    def whisper(self, message, event = None):
        logger.debug(message)
