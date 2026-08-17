import logging

logging.basicConfig(level=logging.DEBUG)# Based on DEBUG, all those are more important than that are also displayed

logging.debug("Debug message")# find mistake
logging.info("User logged in")
logging.warning("This is a warning")
logging.error("An error occurred")
logging.critical("Critical error")# Deadly serious error